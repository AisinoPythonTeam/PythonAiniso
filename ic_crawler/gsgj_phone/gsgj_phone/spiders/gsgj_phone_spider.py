# -*- coding:utf-8 -*-
import re
import time
import json
import string
import hashlib
from scrapy import log
from scrapy.spider import Spider
from scrapy.http import Request, FormRequest

from bson.objectid import ObjectId

from gsgj_phone import settings
from gsgj_phone.util.time_handler import *
from gsgj_phone.items import Item
from gsgj_phone.database.my_mongo import Mongo
from gsgj_phone.util.encode_handle import Encoder
from parser.request_config import get_base_post_paramaters
from parser.json_parse import ParseHandle

class GsgjPhoneSpider(Spider):
    """
        工商总局手机端
        """
    name = 'ic_data'
    query_url = 'http://yd.gsxt.gov.cn/QuerySummary'
    detail_url = 'http://yd.gsxt.gov.cn/QueryBusiLice'

    def __init__(self, source=None):
        self.data = source
        self.json_parse = ParseHandle()

    def start_requests(self):
        search_formdata = get_base_post_paramaters('search_formdata', self.data['company_name'])
        log.msg('list_post_paramaters: %s' % search_formdata, level=log.DEBUG)
        yield FormRequest(url=self.query_url, formdata=search_formdata, headers=settings.DEFAULT_HEADERS, callback=self.parse_list)

    def parse_list(self, response):
        log.msg('response.body __: %s' % response.body, level=log.WARNING)
        companies = json.loads(response.body)
        query_item = None
        items, short_name = self.json_parse.list_parse(companies)
        for item in items:
            if short_name == item['ENTNAME']:
                item['ENTNAME'] = self.data['company_name']
                item['company_md5'] = hashlib.md5(item['ENTNAME'].strip()).hexdigest()
                query_item = item
            else:
                item['company_md5'] = hashlib.md5(item['ENTNAME'].strip()).hexdigest()
        yield FormRequest(url=self.detail_url, meta={'item': query_item}, formdata=query_item['detail_formdata'], headers=settings.DEFAULT_HEADERS, callback=self.parse_detail, errback=self.parse_err)

    def parse_detail(self, response):
        log.msg('_____________code: %s' % response.body, level=log.ERROR) 
        item = response.meta.get('item', None)
        res_json = json.loads(response.body)
        log.msg('%s' % response.body, level=log.WARNING)
        if not res_json:
            self.parse_err('')
            return 
        self.json_parse.detail_parse(item, res_json)
        for k in self.data['json_data']['retData']:
            if k in item and item[k]:
                item[k], c = re.subn('[\{\}]*', '', item[k])
            else:
                continue
            if not self.data['json_data']['retData'][k] or len(self.data['json_data']['retData'][k]) < 4 and item[k]:
                self.data['json_data']['retData'][k] = item[k]
        self.data['json_data']['retData']['crawl_time'] = get_current_date()

        #json_data_str = json.dumps(self.data['json_data'], cls=Encoder)
        #self.redis_db.set_value(self.data['company_md5'], json_data_str)

        #self.mongo_db.ic_data.remove({'_id': ObjectId(self.data['_id'])})
        #retData = self.data['json_data']['retData']
        #base_info

    def parse_err(self, e):
        print e
        status = -1
        try:
            if self.data['json_data']['retData']['company_id']:
                status = 2
        except:
            pass
        #self.mongo_db.ic_data.update({'_id': ObjectId(self.data['_id'])}, {'$set': {'status': status, 'last_crawl_time': int(time.time() * 1000)}})

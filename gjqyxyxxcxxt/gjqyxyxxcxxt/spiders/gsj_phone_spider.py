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

from gjqyxyxxcxxt import settings
from gjqyxyxxcxxt.util._time import *
from gjqyxyxxcxxt.items import GjqyxyxxcxxtItem
from gjqyxyxxcxxt.database.my_mongo import Mongo
from gjqyxyxxcxxt.util.my_encode import Encoder
from parser.general_conf import *
from parser.repeat_handle import RepeatHandle
from parser.parse_handle import ParseHandle

class GsjPhoneSpider(Spider):
    """
        工商总局手机端
        """
    name = 'ic_data'
    url = 'http://www.baidu.com'
    query_url = 'http://yd.gsxt.gov.cn/QuerySummary'
    detail_url = 'http://yd.gsxt.gov.cn/QueryBusiLice'

    def __init__(self, source):
        self.data = source
        self.parse = ParseHandle()
        self.redis_db = RepeatHandle()
        self.mongo_db = Mongo().get_db()
        self.redis_db = RepeatHandle()
        self.mongo_db = Mongo().get_db()

    def start_requests(self):
        search_formdata = base_info('search_formdata', self.data['company_name'])
        log.msg('list_crawl_running => formdata: %s' % search_formdata, level=log.INFO)
        yield FormRequest(url=self.query_url, formdata=search_formdata, headers=settings.DEFAULT_HEADERS, callback=self.parse_list, errback=self.parse_err)

    def parse_list(self, response):
        log.msg('_____________code: %s' % response.body, level=log.ERROR)
        try:
            companies = json.loads(response.body)
            query_item = None
            log.msg('%s' % companies, level=log.WARNING)
            items, short_name = self.parse.list_parse(companies)
            for item in items:
                if short_name == item['ENTNAME']:
                    item['ENTNAME'] = self.data['company_name']
                    item['company_md5'] = hashlib.md5(item['ENTNAME'].strip()).hexdigest()
                    query_item = item
                else:
                    item['company_md5'] = hashlib.md5(item['ENTNAME'].strip()).hexdigest()
            yield FormRequest(url=self.detail_url, meta={'item': query_item}, formdata=query_item['detail_formdata'], headers=settings.DEFAULT_HEADERS, callback=self.parse_detail, errback=self.parse_err)
        except Exception, e:
            self.parse_err(e)

    def parse_detail(self, response):
        log.msg('_____________code: %s' % response.body, level=log.ERROR) 
        item = response.meta.get('item', None)
        res_json = json.loads(response.body)
        log.msg('%s' % response.body, level=log.WARNING)
        if not res_json:
            self.parse_err('')
            return 

        self.parse.detail_parse(item, res_json)
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

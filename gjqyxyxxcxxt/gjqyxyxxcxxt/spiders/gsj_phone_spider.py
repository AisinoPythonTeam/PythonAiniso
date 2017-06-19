# -*- coding:utf-8 -*-
import re
import time
import json
import string
import pymysql
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
        self.mysql_db = pymysql.connect(host="172.16.16.15",port=3306,user="root",passwd="A1s1n0@zxyc#3",db="ixinnuo_sjcj",charset="utf8")

    def start_requests(self):
        search_formdata = base_info('search_formdata', self.data['company_name'])
        log.msg('list_crawl_running => formdata: %s' % search_formdata, level=log.INFO)
        yield FormRequest(url=self.query_url, formdata=search_formdata, headers=settings.DEFAULT_HEADERS, callback=self.parse_list, errback=self.parse_err)

    def parse_list(self, response):
        log.msg('_____________code: %s' % response.status, level=log.ERROR)
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
        log.msg('_____________code: %s' % response, level=log.ERROR) 
        item = response.meta.get('item', None)
        try:
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

            json_data_str = json.dumps(self.data['json_data'], cls=Encoder)
            self.redis_db.set_value(self.data['company_md5'], json_data_str)
        except Exception, e:
            self.parse_err(e)

        self.mongo_db.ic_data.remove({'_id': ObjectId(self.data['_id'])})
        cursor = self.mysql_db.cursor()

        retData = self.data['json_data']['retData']
        #base_info
        b_sql = 'INSERT INTO gsxt_data(ENTNAME, GSZCH, UNISCID, ENTTYPE, LEREP, REGCAP, ESTDATE, DOM, OPFROM, OPTO, REGORG, APPRDATE, REGSTATE, CREATETIME, OPSCOPE) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (
                               retData['ENTNAME'], retData['REGNO'], retData['UNISCID'], retData['ENTTYPE'], retData['LEREP'],
                               (retData['REGCAP']), retData['ESTDATE'], retData['DOM'], retData['OPFROM'], retData['OPTO'],
                               retData['REGORG'], retData['APPRDATE'], retData['REGSTATE'], retData['crawl_time'], retData['OPSCOPE'])
        cursor.execute(b_sql)

        for ryxx in retData['PERINFO']:
            r_sql = 'INSERT INTO gsxt_ryxx (公司名称, 姓名, 职位) VALUES (\'%s\', \'%s\', \'%s\')' % \
                (retData['ENTNAME'].encode('utf-8') if retData['ENTNAME'] else retData['ENTNAME'], 
                    ryxx['NAME'].encode('utf-8') if ryxx['NAME'] else ryxx['NAME'],
                    ryxx['POSITION'].encode('utf-8') if ryxx['POSITION'] else ryxx['POSITION'])
            cursor.execute(r_sql)

        for bgxx in retData['CHGINFO']:
            bg_sql = 'INSERT INTO gsxt_bgxx (公司名称, 变更事项, 变更前内容, 变更后内容, 变更日期) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % \
                        (retData['ENTNAME'].encode('utf-8') if retData['ENTNAME'] else retData['ENTNAME'],
                        bgxx['ALTITEM'].encode('utf-8') if bgxx['ALTITEM'] else bgxx['ALTITEM'],
                        bgxx['ALTBE'].encode('utf-8') if bgxx['ALTBE'] else bgxx['ALTBE'],
                        bgxx['ALTAF'].encode('utf-8') if bgxx['ALTAF'] else bgxx['ALTAF'],
                        bgxx['ALTDATE'].encode('utf-8') if bgxx['ALTDATE'] else bgxx['ALTDATE'])
            cursor.execute(bg_sql)

        for czxx in retData['LEGINFO']:
            czxx_sql = 'INSERT INTO gsxt_gdxx (公司名称, 股东名称, 股东类型, `证照/证件类型`, `证照/证件号码`, 详情) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (
                retData['ENTNAME'], czxx['INV'],'自然人股东',czxx['BLICTYPE'],czxx['BLICNO'],"")
            cursor.execute(czxx_sql)
        self.mysql_db.commit()

    def parse_err(self, e):
        status = -1
        try:
            if self.data['json_data']['retData']['company_id']:
                status = 2
        except:
            pass
        self.mongo_db.ic_data.update({'_id': ObjectId(self.data['_id'])}, {'$set': {'status': status, 'last_crawl_time': int(time.time() * 1000)}})

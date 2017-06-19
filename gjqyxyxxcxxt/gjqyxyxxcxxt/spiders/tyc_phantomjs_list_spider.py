# -*- coding:utf-8 -*-
import re
import time, datetime
import urllib
import json
import string
import hashlib
import pymysql
from scrapy import log
from scrapy.spider import Spider
from scrapy.http import Request

from bson.objectid import ObjectId
from gjqyxyxxcxxt.database.my_mongo import Mongo
from gjqyxyxxcxxt import settings
from parser.general_conf import *
from gjqyxyxxcxxt.util._time import *
from parser.repeat_handle import RepeatHandle
from parser.parse_handle import ParseHandle
from gjqyxyxxcxxt.util.my_encode import Encoder
from bson.objectid import ObjectId
from gjqyxyxxcxxt.database.my_mongo import Mongo

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class PhantomjsListSpider(Spider):
    """
        """
    name = 'ic_list_phantomjs'
    base_url = 'http://www.tianyancha.com/company/'
    mongo_db = Mongo().get_db()
    log.msg('connected', level=log.WARNING)

    def __init__(self, data):
        self.data = data
        #self.json_data = json.loads(data['json_data'])
        #self.data = data

    def start_requests(self):
        yield Request(url='http://127.0.0.1:3000/vietinbanh/query?company_name=%E5%AE%81%E6%B3%A2%E5%94%AF%E7%BF%94%E7%94%B5%E8%84%91%E8%AE%BE%E8%AE%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8', callback=self.parse_list)

    def parse_list(self, response):
        source_company_name = self.data['company_name']
        if isinstance(self.data['company_name'], unicode):
            self.data['company_name'] = self.data['company_name'].encode('utf-8')
        #source = self.parse_phantomjs('http://www.tianyancha.com/search?key=%E5%AE%81%E6%B3%A2%E5%B8%82%E6%B1%9F%E4%B8%9C%E6%97%BA%E6%8D%B7%E5%95%86%E8%B4%B8%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&checkFrom=searchBox')
        source = self.parse_phantomjs('http://www.tianyancha.com/search?key=%s&checkFrom=searchBox' % (urllib.quote(self.data['company_name'])))
        #log.msg('--------->>>: %s' % source, level=log.WARNING)
        res = re.findall('http://www.tianyancha.com/company/(\d+)', source)
        response = response.replace(body=source)
        a_ls = response.xpath(u'//a[@event-name="搜索结果-企业区域"]')
        log.msg('_______>>>: %s' % a_ls.extract(), level=log.WARNING)
        #a_ls = response.xpath('//a[re:test(@href, "http://www\.tianyancha\.com/company/\d+")]')
        items = []
        result_item = None
        is_success = False
        for a in a_ls:
            tyc_ids = a.xpath('@href').re('company/(\d+)')
            company_names = a.xpath('node()').re(u'<em>([^<>]+)</em>')
            log.msg('_______>>>: %s' % tyc_ids, level=log.WARNING)
            log.msg('_______>>>: %s' % company_names, level=log.WARNING)
            if tyc_ids and company_names:
                item = {}
                item['tyc_id'] = tyc_ids[0]
                item['company_name'] = company_names[0]
                items.append(item)
                if is_success is False:
                    if result_item is None or len(result_item['company_name']) > len(item['company_name']):
                         result_item = item
                if not is_success:
                    try:
                        if item['company_name'] == source_company_name:
                            result_item = item
                            is_success = True
                    except:
                        pass
                    try:
                        if item['company_name'].enoce('utf-8') == source_company_name:
                            result_item = item
                            is_success = True
                    except:
                        pass
        for item in items:
            self.mongo_db.ic_list.save(item)
        if result_item:
            self.mongo_db.ic_data.update({'_id': self.data['_id']}, {'$set': {'status': 1, 'json_data': {result_item}}})

    def parse_phantomjs(self, url):
        log.msg('url: %s' % url, level=log.WARNING)
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
            #"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
        )
        driver = webdriver.PhantomJS(executable_path='phantomjs', desired_capabilities=dcap)
        driver.get(url)
        time.sleep(10)
        source = driver.page_source
        body = re.findall(r'<body[^<>]*>[\s\S]+</body>', source)
        try:
            driver.quit()
        except Exception, e:
            driver.quit

        if not body:
            return '<body></body>'
        return body[0]


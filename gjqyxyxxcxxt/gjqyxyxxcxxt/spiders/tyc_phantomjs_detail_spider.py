# -*- coding:utf-8 -*-
import re
import time, datetime

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

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class PhantomjsDetailSpider(Spider):
    """
        """
    name = 'ic_detail_phantomjs'
    base_url = 'http://www.tianyancha.com/company/'

    def __init__(self, data):
        self.json_data = json.loads(data['json_data'])
        self.data = data

    def start_requests(self):
        yield Request(url='http://www.baidu.com', callback=self.parse_base_info)

    def parse_base_info(self, response):
        retData = self.json_data['retData']
        log.msg(u'开始diaoyong！', level=log.WARNING)
        source = self.parse_phantomjs(retData['company_id'])
        response = response.replace(body=source)
        log.msg(u'开始caiji！', level=log.WARNING)

        detail = response.xpath(u'//a[@event-name="企业详情-法人"]')
        if detail:
            LEREP = detail[0].xpath('text()').extract()
            if LEREP:
                retData['LEREP'] = LEREP[0] if LEREP else None
            REGCAP = detail[0].xpath('../../td[2]/div/text()').extract()
            if REGCAP:
                retData['REGCAP'] = REGCAP[0] if REGCAP else None
            ESTDATE = detail[0].xpath('../../td[3]/div/text()').extract()
            if ESTDATE:
                retData['ESTDATE'] = ESTDATE[0] if ESTDATE else None
            REGSTATE = detail[0].xpath('../../td[4]/div/text()').extract()
            if REGSTATE:
                retData['REGSTATE'] = REGSTATE[0] if REGSTATE else None

        #ENTNAME = response.xpath(u'//div[contains(@class, "company-content")]/descendant::*/div[@class="c8"][re:test(text(), "工商注册号")]/span/text()').extract()
        OPSCOPE = response.xpath(u'//div[contains(@class, "company-content")]/descendant::*/div[@class="c8"][re:test(text(), "经营范围")]/span/text()').extract()
        DOM = response.xpath(u'//div[contains(@class, "company-content")]/descendant::*/div[@class="c8"][re:test(text(), "注册地址")]/span/text()').extract()
        
        REGNO = response.xpath(u'//div[contains(@class, "company-content")]/descendant::*/div[@class="c8"][re:test(text(), "工商注册号")]/span/text()').extract()
        ORGAN_CODE = response.xpath(u'//div[contains(@class, "company-content")]/descendant::*/div[@class="c8"][re:test(text(), "组织机构代码")]/span/text()').extract()
        UNISCID = response.xpath(u'//div[contains(@class, "company-content")]/descendant::*/div[@class="c8"][re:test(text(), "统一信用代码")]/span/text()').extract()
        APPRDATE = response.xpath(u'//div[contains(@class, "company-content")]/descendant::*/div[@class="c8"][re:test(text(), "核准日期")]/span/text()').extract()
        REGORG = response.xpath(u'//div[contains(@class, "company-content")]/descendant::*/div[@class="c8"][re:test(text(), "登记机关")]/span/text()').extract()
        ENTTYPE = response.xpath(u'//div[contains(@class, "company-content")]/descendant::*/div[@class="c8"][re:test(text(), "企业类型")]/span/text()').extract()
        OPTO = response.xpath(u'//div[contains(@class, "company-content")]/descendant::*/div[@class="c8"][re:test(text(), "营业期限")]/span/text()').extract()

        retData['OPSCOPE'] = OPSCOPE[0] if OPSCOPE else None
        retData['DOM'] = DOM[0] if DOM else None
        retData['REGCAP'] = REGCAP[0] if REGCAP else None

        retData['REGNO'] = REGNO[0] if REGNO else None
        retData['ORGAN_CODE'] = ORGAN_CODE[0] if ORGAN_CODE else None
        retData['UNISCID'] = UNISCID[0] if UNISCID else None
        retData['APPRDATE'] = APPRDATE[0] if APPRDATE else None
        retData['REGORG'] = REGORG[0] if REGORG else None
        retData['ENTTYPE'] = ENTTYPE[0] if ENTTYPE else None
        retData['OPTO'] = OPTO[0] if OPTO else None
        log.msg('>>>>>>>%s' % retData, level=log.WARNING)

        if not (REGNO or ORGAN_CODE or UNISCID or APPRDATE or REGORG or ENTTYPE or OPTO):
            return None

        if retData['OPTO']:
            opfrom = re.findall(u'(.+?)至', retData['OPTO'])
            res = re.findall(u'至(\d{4}\D\d{1,2}\D\d{1,2}\D?$)', retData['OPTO'])
            if not res:
                res = re.findall(u'至(\D+)', retData['OPTO'])
            if res:
                retData['OPTO'] = res[0]
            res = opfrom
            if res:
                retData['OPFROM'] = res[0]

        if retData['APPRDATE']:
            res = re.findall(u'\d{4}\D\d{1,2}\D\d{1,2}', retData['APPRDATE'])
            if res:
                retData['APPRDATE'] = res[0]

        if retData['ESTDATE']:
            res = re.findall(u'\d{4}\D\d{1,2}\D\d{1,2}', retData['ESTDATE'])
            if res:
                retData['ESTDATE'] = res[0]
        retData['crawl_time'] = get_current_date()

        self.json_data['retData'] = retData

        redis_db = RepeatHandle()
        mongo_db = Mongo().get_db()
        mysql_db = pymysql.connect(host="172.16.16.15",port=3306,user="root",passwd="A1s1n0@zxyc#3",db="ixinnuo_sjcj",charset="utf8")
        cursor = mysql_db.cursor()

        log.msg(u'开始save', level=log.WARNING)
        json_data_str = json.dumps(self.json_data, cls=Encoder)
        redis_db.set_value(self.data['company_md5'], json_data_str)
        mongo_db.ic_data.remove({'_id': ObjectId(self.data['_id'])})
        
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
        mysql_db.commit()

    def parse_phantomjs(self, c_id):
        url = "http://www.tianyancha.com/company/%s" % c_id
        log.msg(u'----->>>>url: %s' % url, level=log.WARNING)
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
        )
        driver = webdriver.PhantomJS(executable_path='phantomjs', desired_capabilities=dcap)
        driver.get(url)
        time.sleep(8)
        source = driver.page_source
        body = re.findall(r'<body[^<>]*>[\s\S]+</body>', source)
        try:
            driver.quit()
        except Exception, e:
            driver.quit

        if not body:
            return '<body></body>'
        return body[0]



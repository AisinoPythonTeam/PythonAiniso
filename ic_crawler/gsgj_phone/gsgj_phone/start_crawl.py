# -*- coding:utf-8 -*-
"""
    多进程方式生成crawler
    """
import sys, os
#免去环境变量配置
app_dir = os.path.abspath("../")
sys.path.append(app_dir)

reload(sys)
sys.setdefaultencoding( "utf-8" )

import time, yaml, json, re
from scrapy import log
from scrapy import signals
from scrapy.crawler import Crawler
from twisted.internet import reactor
from scrapy.utils.project import get_project_settings
#MONGO
import pymongo
from bson.objectid import ObjectId
from gsgj_phone.database.my_mongo import Mongo

from spiders.gsgj_phone_spider import GsgjPhoneSpider
from gsgj_phone import settings
from util.encode_handle import Encoder

""" 
    初始化所有站点 
    @采集时间控制来至：队列
    @采集配置控制来至：配置文件
    """

def sys_exit(s):
    print '%s秒后系统退出!!!' % s
    time.sleep(s)
    exit()

def forever_run():
    """ 不断启动进程、查询队列、初始化站点
        """
    mongo_db = Mongo().get_db()
    # query
    results = list(mongo_db.ic_data.find({"status" : 0}).sort([('last_crawl_time', pymongo.ASCENDING)]).limit(1))
    if not results:
        print '无需要采集的数据源!!!'
        sys_exit(3)
    time.sleep(2)

    spiders = []
    for result in results:
        print result
        json_data = result['json_data']
        mongo_db.ic_data.update({'_id': ObjectId(result['_id'])}, {'$set': {'status': 0, 'part_gsj': True, 'last_crawl_time': int(time.time())}})
        create_spider(result)
        spiders.append(1)
        log.start(logfile='%s' % settings.LOG_FILE, loglevel=settings.LOG_LEVEL)
        if not spiders:
            sys_exit(3)
    if spiders:
        reactor.run()

def create_spider(result):
    """创建采集器、多线程在采集器里生成
        """
    spider = GsgjPhoneSpider(result)
    crawler = Crawler(get_project_settings())
    crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()
    print 'start '

if __name__ == '__main__':
    forever_run()
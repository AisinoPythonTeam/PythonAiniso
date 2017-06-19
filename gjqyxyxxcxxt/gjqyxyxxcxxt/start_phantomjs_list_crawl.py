# -*- coding:utf-8 -*-
"""
    多进程方式生成crawler
    """
import sys
import os
#免去环境变量配置
app_dir = os.path.abspath("../")
sys.path.append(app_dir)

reload(sys)
sys.setdefaultencoding( "utf-8" )

import time, yaml, json, re, click
from scrapy import log
from scrapy import signals
from scrapy.crawler import Crawler
from twisted.internet import reactor

#MONGO
import pymongo
from bson.objectid import ObjectId
from gjqyxyxxcxxt.database.my_mongo import Mongo

from scrapy.utils.project import get_project_settings
from spiders.tyc_phantomjs_list_spider import PhantomjsListSpider
from gjqyxyxxcxxt import settings
""" 
    初始化所有站点 
    @采集时间控制来至：队列
    @采集配置控制来至：配置文件
    """

def sys_exit(s):
    print '%s秒后系统退出!!!' % s
    exit()

@click.command()
@click.option('--company_name', default=None, help='entry company to crawl')
def forever_run(company_name):
    time.sleep(3)
    print company_name
    """ 不断启动进程、查询队列、初始化站点
        """
    #if company_name is None:
    #    return

    mongo_db = Mongo().get_db()
    datas = list(mongo_db.ic_data.find({'status': 0}).sort([('last_crawl_time', pymongo.ASCENDING)]).limit(1))
    print 'mongod 查询结果: %s' % len(datas)
    print '----->>>', datas[0]
    if not datas:
        sys_exit(3)
    data = datas[0]

    create_spider(data)
    log.start(logfile='%s' % settings.LOG_FILE, loglevel=settings.LOG_LEVEL)
    reactor.run()

def create_spider(data):
    """创建采集器、多线程在采集器里生成
        """
    print 'create_spider '
    spider = PhantomjsListSpider(data)
    crawler = Crawler(get_project_settings())
    print 'create_spider 2'
    crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
    print 'create_spider 3'
    crawler.configure()
    print 'create_spider 4'
    crawler.crawl(spider)
    print 'create_spider 5'
    crawler.start()
    print 'start '

if __name__ == '__main__':
    forever_run(None)



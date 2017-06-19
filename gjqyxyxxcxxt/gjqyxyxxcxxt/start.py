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

import time, yaml, json, re
from scrapy import log
from scrapy import signals
from scrapy.crawler import Crawler
from twisted.internet import reactor
from scrapy.utils.project import get_project_settings
#MYSQL
import pymysql
#MONGO
import pymongo
from bson.objectid import ObjectId
from gjqyxyxxcxxt.database.my_mongo import Mongo
#redis
from spiders.parser.repeat_handle import RepeatHandle

from spiders.parser.tyc_dispatcher import run
from spiders.gsj_phone_spider import GsjPhoneSpider

from gjqyxyxxcxxt import settings
from util.my_encode import Encoder

from filed_conf import *
""" 
    初始化所有站点 
    @采集时间控制来至：队列
    @采集配置控制来至：配置文件
    """

def sys_exit(s):
    time.sleep(s)
    print '%s秒后系统退出!!!' % s
    exit()

def forever_run():
    """ 不断启动进程、查询队列、初始化站点
        """
    mongo_db = Mongo().get_db()
    mysql_db = pymysql.connect(host="172.16.16.15",port=3306,user="root",passwd="A1s1n0@zxyc#3",db="ixinnuo_sjcj",charset="utf8")
    redis_db = RepeatHandle()

    results = list(mongo_db.ic_data.find({"status" : 1}).sort([('last_crawl_time', pymongo.ASCENDING)]).limit(1))

   
    """
    results1 = list(mongo_db.ic_data.find({'status': -1}).sort([('last_crawl_time', pymongo.ASCENDING)]))
    for res in results1:
        add_company_name_to_req(mysql_db, res['company_name'])
        mongo_db.ic_data.update({'_id': res['_id']}, {'$set': {'status': -2}})
    print results
    """

    if not results:
        print '无需要采集的数据源!!!'
        sys_exit(3)
    
    time.sleep(3)

    spiders = []
    a = 0
    for data in results:
        #json_data = init_handle()
        print data
        res = {}
        json_data = data['json_data']
        print json_data
        if json_data and 'company_url' in json_data:
            tyc_id = re.findall('company/(\d+$)', json_data['company_url'])
            print tyc_id
            if tyc_id:
                res = run(tyc_id[0])
                print '_____________:', res
        if res:
            json_data['CHGINFO'] = res.get('CHGINFO', [])
            json_data['LEGINFO'] = res.get('LEGINFO', [])
            json_data['PERINFO'] = res.get('PERINFO', [])
            json_data['BRANINFO'] = res.get('BRANINFO', [])
            json_data['MORTINFO'] = res.get('MORTINFO', [])
            json_data['EXCEINFO'] = res.get('EXCEINFO', [])
            json_data['PUNINFO'] = res.get('PUNINFO', [])
            item = {}
            item['retData'] = json_data
            item['errNum'] = 0
            item['abstract'] = ""
            item['userID'] = ""
            item['timeStamps'] = int(time.time())
            item['errMsg'] = "success"
            json_data_str = json.dumps(item, cls=Encoder)
            redis_db.set_value(data['company_md5'], json_data_str)
            mongo_db.ic_data.update({'_id': ObjectId(data['_id'])}, {'$set': {'status': 3, 'json_data': json_data_str, 'part_tyc': True, 'last_crawl_time': int(time.time() * 1000)}})

        """
        data['json_data'] = json_data
        #获取天眼查JSON数据\其他作为补充
        if data['part_tyc'] is False and data['status'] == 1:
            print '>>>1  start_get_tyc_data'
            print data['company_name']
            
            #print data['company_name']
            data['json_data']['retData'] = tyc_item
            json_data_str = json.dumps(data['json_data'], cls=Encoder)
            print json_data_str
            mongo_db.ic_data.update({'_id': ObjectId(data['_id'])}, {'$set': {'status': 2, 'json_data': json_data_str, 'part_tyc': True, 'last_crawl_time': int(time.time() * 1000)}})
        
        #方案一：取mysql_数据库
            #不用存mysql
       
        print '>>>2  start_get_mysql_data'
        cursor = mysql_db.cursor()
        get_info_from_mysql(cursor, data)
        print data
        if data['status'] == 1:
            json_data_str = json.dumps(data['json_data'], cls=Encoder)
            redis_db.set_value(data['company_md5'], json_data_str)
            mongo_db.ic_data.remove({'_id': ObjectId(data['_id'])})
            return

        #方案二：取工商局公司连接
        #由于链接一直在变且会很快失效，所有不能通过固定链接去采集，该方案先搁浅
        #注意有的需要到地方链接上采集

        '''
        if data['company_url']:
            spiders = []
            create_spider(data, GsjSpider)
            spiders.append(1)
            log.start(logfile='%s' % settings.LOG_FILE, loglevel=settings.LOG_LEVEL)
            if not spiders:
                sys_exit(2)
            reactor.run()
        

        #方案三：取工商局手机端基本信息
        # 稳定性太差

        print '>>>3 start_get_gsj_phone_data'
        spiders = []
        mongo_db.ic_data.update({'_id': ObjectId(data['_id'])}, {'$set': {'last_crawl_time': int(time.time() * 1000)}})
        create_spider(data, GsjPhoneSpider)
        spiders.append(1)
        log.start(logfile='%s' % settings.LOG_FILE, loglevel=settings.LOG_LEVEL)
        if not spiders:
            sys_exit(2)
        reactor.run()
        '''
        #方案四：取天眼查基本信息
        #tyc_crawler()
        ##存mysql
        """

if __name__ == '__main__':
    forever_run()


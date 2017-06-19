# -*- coding:utf-8 -*-
"""
    多进程方式生成crawler
    """
import sys
import os
#免去环境变量配置
app_dir = os.path.abspath("/data/crawler/gjqyxyxxcxxt")
sys.path.append(app_dir)

reload(sys)
sys.setdefaultencoding( "utf-8" )
import click
import hashlib
import time, yaml, json, re
#MYSQL
import pymysql
#MONGO
import pymongo
from bson.objectid import ObjectId
from gjqyxyxxcxxt.database.my_mongo import Mongo
#redis
from spiders.parser.repeat_handle import RepeatHandle

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

@click.command()
@click.option('--company_name', default=None, help='entry company to crawl')
def forever_run(company_name):
    """ 不断启动进程、查询队列、初始化站点
        """
    
    mongo_db = Mongo().get_db()
    mysql_db = pymysql.connect(host="172.16.16.15",port=3306,user="root",passwd="A1s1n0@zxyc#3",db="ixinnuo_sjcj",charset="utf8")
    redis_db = RepeatHandle()

    if not company_name:
        print '请输入公司名称'
        return
    
    md5 = hashlib.md5(company_name).hexdigest()

    res = redis_db.get_key(md5)
    obj = {
    "retData": {
        "OPSCOPE": "生产、加工TFT-LCD用SMT、PCB等新型平板显示器件，销售自产产品及TFT-LCD用SMT、PCB等新型平板显示元器件的进出口批发业务，并提供相关服务（涉及法律、法规禁止经营的不得经营，涉及许可证经营的凭许可证经营）；普通货物道路运输。（依法须经批准的项目，经相关部门批准后方可开展经营活动）",
        "ENTNAME": "智水电子（南京）有限公司",
        "REGORG": None,
        "DOM": "南京经济技术开发区恒飞路15号",
        "company_url": "http://www.tianyancha.com/company/2350425668",
        "EXCEINFO": [],
        "EMAIL": " CW62002@njzhishui.com",
        "OPTO": "2055-01-17 ",
        "TEL": " 025-85805798",
        "LEGINFO": [
            {
                "INVTYPE": "",
                "INVDETAIL": {
                    "INV": "江苏南极星科技有限公司",
                    "REALPAYINFO": [],
                    "LIACCONAM": None,
                    "PAYINFO": [
                        {
                            "SUBCONAM": "5627万元人民币",
                            "CONFORM": None,
                            "CONDATE": None
                        }
                    ],
                    "LISUBCONAM": 0
                },
                "INV": "江苏南极星科技有限公司",
                "BLICNO": "",
                "FLAG": "",
                "ID": 2333760342,
                "BLICTYPE": ""
            }
        ],
        "CHGINFO": [
            {
                "ALTDATE": "2016-07-11",
                "ALTITEM": "经营范围",
                "ALTBE": "生产、加工-用、等新型平板显示器件，销售自产产品及-用、等新型平板显示元器件的进出口批发业务，并提供相关服务（涉及法律、法规禁止经营的不得经营，涉及许可证经营的凭许可证经营）。（依法须经批准的项目，经相关部门批准后方可开展经营活动）",
                "ALTAF": "生产、加工-用、等新型平板显示器件，销售自产产品及-用、等新型平板显示元器件的进出口批发业务，并提供相关服务（涉及法律、法规禁止经营的不得经营，涉及许可证经营的凭许可证经营）；普通货物道路运输。（依法须经批准的项目，经相关部门批准后方可开展经营活动）"
            },
            {
                "ALTDATE": "2015-06-08",
                "ALTITEM": "注册资本变更",
                "ALTBE": "725.000000",
                "ALTAF": "5627.000000"
            },
            {
                "ALTDATE": "2015-06-08",
                "ALTITEM": "股东变更",
                "ALTBE": "韩国株式会社",
                "ALTAF": "江苏南极星科技有限公司"
            },
            {
                "ALTDATE": "2015-06-08",
                "ALTITEM": "法定代表人变更",
                "ALTBE": "具滋燮",
                "ALTAF": "胡毓晓"
            },
            {
                "ALTDATE": "2015-06-08",
                "ALTITEM": "企业类型变更",
                "ALTBE": "有限责任公司(外国法人独资)",
                "ALTAF": "有限责任公司(自然人投资或控股的法人独资)"
            }
        ],
        "APPRDATE": " 2016-07-11",
        "OPFROM": " 2005-01-18",
        "REGCAP": "5627万元人民币",
        "company_name": "智水电子（南京）有限公司",
        "REGSTATE": "在业",
        "ENTTYPE": "有限责任公司（法人独资）",
        "PUNINFO": [],
        "MORTINFO": [],
        "COMPANY_URL": " www.njzhishui.com",
        "PERINFO": [
            {
                "POSITION": "监事",
                "NAME": "张升大"
            },
            {
                "POSITION": "执行董事, 总经理",
                "NAME": "胡毓晓"
            }
        ],
        "LEREP": "胡毓晓",
        "ESTDATE": "2005-01-18",
        "UNISCID": "9132010076818306XQ",
        "BRANINFO": [],
        "ORGAN_CODE": "76818306X",
        "REGNO": "320100400028410"
    },
    "errNum": 0,
    "abstract": "",
    "userID": "",
    "timeStamps": 1497850306,
    "errMsg": "success"
}
    
    print obj
    json_data_str = json.dumps(obj, cls=Encoder)
    redis_db.set_value(md5, json_data_str)

if __name__ == '__main__':
    forever_run()

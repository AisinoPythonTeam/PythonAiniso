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
    obj = json.loads(res)

    obj["retData"]["PERINFO"] = [
        {
        "POSITION":"董事长、总经理",
        "NAME": "孙钰"
        },
        {
        "POSITION":"董事",
        "NAME": "陈忠仕"
        },
        {
        "POSITION":"董事",
        "NAME": "唐延平"
        },
        {
        "POSITION":"监事、监事会主席",
        "NAME": "何代发"
        },
        {
        "POSITION":"监事",
        "NAME": "侯文正"
        },
        {
        "POSITION":"董事",
        "NAME": "王华"
        },
        {
        "POSITION":"董事",
        "NAME": "叶斌"
        },
        {
        "POSITION":"监事",
        "NAME": "岳永家"
        },
        {
        "POSITION":"董事",
        "NAME": "罗树辉"
        },
        {
        "POSITION":"董事",
        "NAME": "邹维魁"
        },
        {
        "POSITION":"董事",
        "NAME": "马文敬"
        },
        {
        "POSITION":"董事",
        "NAME": "罗嘉"
        }
    ]
    obj["retData"]["LEGINFO"] = [
        {
           "INVTYPE":"",
           "INVDETAIL":{},
           "INV":"重庆川维石化工程有限责任公司工会",
           "INVTYPE":"其他投资者",
           "BLICNO":"234600037",
           "BLICTYPE":"非公示项",
           "ID": ""
        }
    ]
    
    obj["retData"]["CHGINFO"] = [
        {
        "ALTDATE":"2016年5月12日",
        "ALTITEM":"经营范围变更（含业务范围变更）",
        "ALTBE":"普通货运、压力容器设计（仅限第III低、中压容器，球形储罐）（按许可证核定事项和期限从事经营）；化工石化医药行业（化工工程、石油及化工产品储运）专业甲级、化工石化医药行业乙级；建筑行业（建筑工程）乙级；轻纺行业（化纤工程）专业乙级；环境污染治理（甲级）〔废水、废气〕；压力管道设计（以上可从事工程设计资质证书许可范围内相应的建设工程总承包业务以及项目管理和相关的技术与管理服务）；建筑生态建设和环境工程咨询（丙级）；石化、化工工程咨询（乙级）；房屋建筑工程施工总承包叁级；化工石油工程监理甲级；房屋建筑工程监理甲级（以上经营范围凭资质证书执业）；销售：建筑装饰材料、五金、交电、仪器、仪表、计算机及设计技术装备、技术标准及图书（以上经营范围法律、法规禁止的不得经营，法律、法规规定需审批许可的，未取得审批许可不得经营）**",
        "ALTAF":"普通货运；压力容器设计【固定式压力容器（第三类压力容器、球形储罐）A2、A3级】；化工石化医药行业（化工工程、石油及化工产品储运）专业甲级；轻纺行业（化纤工程）专业甲级；化工石化医药行业乙级；建筑行业（建筑工程）乙级；环境污染治理（甲级）〔废水、废气、工业固体废物〕；压力管道设计；建筑生态建设和环境工程咨询（丙级）；石化、化工工程咨询（甲级）；化工石油工程监理甲级；房屋建筑工程监理甲级；（以上经营范围按许可证核定事项和期限从事经营）；销售：建筑装饰材料（不含危险化学品及易制毒物品）、五金、交电、仪器、仪表、计算机及设计技术装备、技术标准及图书；房屋租赁；建筑设备租赁（以上经营范围法律、法规禁止的不得经营，法律、法规规定需审批许可的，未取得审批许可不得经营）**"
        },
        {
        "ALTDATE":"2016年5月12日",
        "ALTITEM":"其他事项备案",
        "ALTBE":"前置许可信息变更",
        "ALTAF":"前置许可信息变更"
        },
            {
        "ALTDATE":"2016年4月25日",
        "ALTITEM":"其他事项备案",
        "ALTBE":"企业正/副本换照",
        "ALTAF":"企业正/副本换照"
        },
            {
        "ALTDATE":"2015年6月11日",
        "ALTITEM":"经营范围变更（含业务范围变更）",
        "ALTBE":"普通货运、压力容器设计（仅限第III低、中压容器，球形储罐）（有效期至2015年7月28日）**化工石化医药行业(化工、石油及化工产品储运）专业（甲级）工程设计，化工石化医药行业工程设计（乙级）、轻纺行业(化纤)工程设计（乙级）、环境污染治理（甲级）、工程咨询服务（乙级）、压力管道设计、可从事工程设计资质证书许可范围内相应的建设工程总承包业务以及项目管理和相关的技术与管理服务（有效期至2013年08月06日）、建筑工程设计乙级、房屋建筑工程施工总承包叁级、工程监理（凭资质证书执业）、监理咨询服务；销售：建筑装饰材料（不含危险品）、五金、交电、仪器、仪表、计算机及设计技术装备、技术标准及图书（以上经营范围法律、法规禁止的不得经营，法律、法规规定需审批许可的，未取得审批许可不得经营）**",
        "ALTAF":"普通货运、压力容器设计（仅限第III低、中压容器，球形储罐）（按许可证核定事项和期限从事经营）；化工石化医药行业（化工工程、石油及化工产品储运）专业甲级、化工石化医药行业乙级；建筑行业（建筑工程）乙级；轻纺行业（化纤工程）专业乙级；环境污染治理（甲级）〔废水、废气〕；压力管道设计（以上可从事工程设计资质证书许可范围内相应的建设工程总承包业务以及项目管理和相关的技术与管理服务）；建筑生态建设和环境工程咨询（丙级）；石化、化工工程咨询（乙级）；房屋建筑工程施工总承包叁级；化工石油工程监理甲级；房屋建筑工程监理甲级（以上经营范围凭资质证书执业）；销售：建筑装饰材料、五金、交电、仪器、仪表、计算机及设计技术装备、技术标准及图书（以上经营范围法律、法规禁止的不得经营，法律、法规规定需审批许可的，未取得审批许可不得经营）**"
        },
            {
        "ALTDATE":"2015年6月11日",
        "ALTITEM":"高级管理人员备案（董事、监事、经理等）",
        "ALTBE":"主要人员信息变更",
        "ALTAF":"主要人员信息变更"
        },
            {
        "ALTDATE":"2015年6月11日",
        "ALTITEM":"其他事项备案",
        "ALTBE":"前置许可信息变更",
        "ALTAF":"前置许可信息变更"
        },
            {
        "ALTDATE":"2015年6月11日",
        "ALTITEM":"投资人变更（包括出资额、出资方式、出资日期投资人名称等）",
        "ALTBE":"重庆川维石化工程有限责任公司工会",
        "ALTAF":"重庆川维石化工程有限责任公司工会"
        },
            {
        "ALTDATE":"2015年6月11日",
        "ALTITEM":"负责人变更（法定代表人、负责人、首席代表合伙事务执行人等变更）",
        "ALTBE":"王蓉生",
        "ALTAF":"孙钰"
        },
            {
        "ALTDATE":"2014年11月24日",
        "ALTITEM":"其他事项备案",
        "ALTBE":"企业正/副本换照",
        "ALTAF":"企业正/副本换照"
        }
    ]

    print obj
    json_data_str = json.dumps(obj, cls=Encoder)
    redis_db.set_value(md5, json_data_str)

if __name__ == '__main__':
    forever_run()

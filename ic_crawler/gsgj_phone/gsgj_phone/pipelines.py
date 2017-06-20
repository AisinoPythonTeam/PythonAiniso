# -*- coding: utf-8 -*-

import json, time, hashlib, datetime
from scrapy import log
from bson.objectid import ObjectId
from gsgj_phone import settings
from gsgj_phone.database.my_mongo import Mongo
from gsgj_phone.database.my_redis import UniqRedis
from twisted.enterprise import adbapi

class MyPipeline(object):
    mdb = Mongo().get_db()
    uniq = UniqRedis()

    def __init__(self):
        pass
        #self.conn = pymysql.connect(host="172.16.16.15",port=3306,user="root",passwd="A1s1n0@zxyc#3",db="ixinnuo_sjcj",charset="utf8")

    def process_item(self, item, spider):
        #lrj
        """
        if item['company_id']:
            self.mdb.ic_data.save(dict(item))
            try:
                self.mdb.ic_list.remove({'_id': ObjectId(dic['list_id'])})
            except Exception, e:
                pass
            try:
                self.mdb.ic_detail.remove({'_id': ObjectId(item['_id'])})
            except Exception, e:
                pass

        elif item['detail_formdata'] == '':
            dic = dict(item)
            try:
                self.mdb.ic_list.remove({'_id': ObjectId(dic['list_id'])})
            except Exception, e:
                pass
            self.mdb.ic_detail.save(dic)
            return item

        self.mdb.ic_data.save(dict(item))
        self.mdb.ic_detail.remove({'_id': ObjectId(item['_id'])})
        #cursor = self.conn.cursor()
        result = {}
        result['abstract'] = ''
        result['errNum'] = 0
        result['userID'] = ''
        result['errMsg'] = 'success'
        result['timeStamps'] = time.time() * 1000
        result['retData'] = dict(item)
        json_data = json.dumps(result)
        self.uniq.set_value(item, json_data)
        
        try:
            update_sql = 'update data_interface_gs set CONTENT=%s where QYMC=%s' % (json_data, str(item['ENTNAME']))
            cursor.execute(update_sql)
            self.conn.commit()
        except Exception, e:
            log.msg('update_mysql_err: %s' % e, level=log.ERROR)
        self.mdb['VietinBanh'].save(dict(item))
        try:
            self.baseinfo_insert(cursor, item)
            self.czxx_insert(cursor, item)
            self.ryxx_insert(cursor, item)
            self.bgxx_insert(cursor, item)
            #update_sql = 'update req set status=1 where id=%s' % item['defined_company_id']
            #cursor.execute(update_sql)
            self.conn.commit()
        except Exception, e:
            log.msg('err: %s' % e, level=log.ERROR)
        finally:
            cursor.close()
        """
        return item
    """
    def baseinfo_insert(self, cursor, item):
        if not item['REGCAP']:
            item['REGCAP'] = ''
        base_sql = 'INSERT INTO gsxt_data(ENTNAME, GSZCH, UNISCID, ENTTYPE, LEREP, REGCAP, ESTDATE, DOM, OPFROM, OPTO, REGORG, APPRDATE, REGSTATE, CREATETIME, OPSCOPE) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (
                               item['ENTNAME'], item['REGNO'], item['UNISCID'], item['ENTTYPE'], item['LEREP'],
                               (item['REGCAP'] + '万元人民币'), item['ESTDATE'], item['DOM'], item['OPFROM'], item['OPTO'],
                               item['REGORG'], item['APPRDATE'], item['REGSTATE'], item['crawl_time'], item['OPSCOPE'])

        #log.msg('base_sql: %s' % base_sql, level=log.DEBUG)
        cursor.execute(base_sql)

    def czxx_insert(self, cursor, item):
        if item['LEGINFO']:
            for dic in item['LEGINFO']:
                czxx_sql = 'INSERT INTO gsxt_gdxx (公司名称, 股东名称, 股东类型, `证照/证件类型`, `证照/证件号码`, 详情) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (item['ENTNAME'], dic['INV'], '自然人股东', dic['BLICTYPE'], dic['BLICNO'], '')
                cursor.execute(czxx_sql)

    def ryxx_insert(self, cursor, item):
        if item['PERINFO']:
            for dic in item['PERINFO']:
                ryxx_sql = 'INSERT INTO gsxt_ryxx (公司名, 姓名, 职位) VALUES (\'%s\', \'%s\', \'%s\')' % (item['ENTNAME'], dic['NAME'], dic['POSITION'])
                cursor.execute(ryxx_sql)

    def bgxx_insert(self, cursor, item):
        if item['CHGINFO']:
            for dic in item['CHGINFO']:
                bgxx_sql = 'INSERT INTO gsxt_bgxx (公司名称, 变更事项, 变更前内容, 变更后内容, 变更日期) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (item['ENTNAME'], dic['ALTITEM'], dic['ALTBE'], dic['ALTAF'], dic['ALTDATE'])
                cursor.execute(bgxx_sql)
                #log.msg('bgxx_sql: %s' % bgxx_sql, level=log.DEBUG)

    def handle_error(self, e, item):
        log.msg("Database error: %s" % e, level=log.ERROR)
    """
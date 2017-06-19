# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re, json, time, codecs, urllib, requests, pymysql

def get_current_date():
    currtime = time.localtime(time.time())
    date = time.strftime('%Y-%m-%d',currtime)
    timer = time.strftime('%H:%M:%S')
    T = date + " " + timer
    return T

class AddToMysql():
    mysql_db = pymysql.connect(host="172.16.16.15",port=3306,user="root",passwd="A1s1n0@zxyc#3",db="ixinnuo_sjcj",charset="utf8")

    def get_company_info_from_mysql(self):
        names = []
        cursor = self.mysql_db.cursor()
        cursor.execute('SELECT entname FROM req WHERE status=0 ORDER BY id')
        results = cursor.fetchall()
        print len(results)
        names.append('慧与软件(济宁)人才产业基地管理有限公司')
        for result in results:
            names.append(result[0])

        for name in names:
            res = requests.get('http://192.168.9.70:3000/vietinbanh/query?company_name=%s' % name)
            try:
                res = res.json()
                if res is None:
                    continue
            except:
                continue
            retData = res['retData']
            print retData['ENTNAME']
            b_sql = 'INSERT INTO gsxt_data(ENTNAME, GSZCH, UNISCID, ENTTYPE, LEREP, REGCAP, ESTDATE, DOM, OPFROM, OPTO, REGORG, APPRDATE, REGSTATE, CREATETIME, OPSCOPE) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (
                                retData['ENTNAME'], retData['REGNO'], retData['UNISCID'], retData['ENTTYPE'], retData['LEREP'],
                                (retData['REGCAP']), retData['ESTDATE'], retData['DOM'], retData['OPFROM'], retData['OPTO'],
                                retData['REGORG'], retData['APPRDATE'], retData['REGSTATE'], get_current_date(), retData['OPSCOPE'])
            cursor.execute(b_sql)
            for ryxx in retData['PERINFO']:
                print(retData['ENTNAME'])
                print(ryxx['NAME'])
                print(ryxx['POSITION'])

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

            update_sql = 'UPDATE req SET status=1 WHERE ENTNAME=\"' + name + '\"'
            print(update_sql)
            cursor.execute(update_sql)
            self.mysql_db.commit()

        for name in names:
            if name:
                print name
                res = requests.get('http://192.168.9.70:3000/vietinbanh/crawler?company_name=%s' % name)
                print res.text
                time.sleep(5)

if __name__ == '__main__':
    gsj = AddToMysql()
    gsj.get_company_info_from_mysql()


# -*- coding:utf-8 -*-
import re, json, time, codecs, urllib, requests, pymysql
class GsjApi():
    mysql_db = pymysql.connect(host="172.16.16.15",port=3306,user="root",passwd="A1s1n0@zxyc#3",db="ixinnuo_sjcj",charset="utf8")

    def get_company_info_from_mysql(self):
        names = []
        cursor = self.mysql_db.cursor()
        cursor.execute('SELECT id, entname FROM req WHERE status=0 ORDER BY id limit 100')
        results = cursor.fetchall()
        print len(results)
        for result in results:
            names.append(result[1])

        for name in names:
            res = requests.get('http://192.168.9.70:3000/vietinbanh/crawler?company_name=%s' % name)
            print res.text
            time.sleep(5)

        time.sleep(5)
        for name in names:
            res = requests.get('http://192.168.9.70:3000/vietinbanh/query?company_name=%s' % name)
            print res.text
if __name__ == '__main__':
    gsj = GsjApi()
    gsj.get_company_info_from_mysql()
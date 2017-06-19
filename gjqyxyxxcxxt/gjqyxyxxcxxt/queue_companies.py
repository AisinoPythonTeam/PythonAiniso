# -*- coding: utf-8 -*-
import pymysql
import sys, os, json, time, pymongo
app_dir = os.path.abspath("../")
sys.path.append(app_dir)

from gjqyxyxxcxxt import settings
from gjqyxyxxcxxt.database.my_redis import QueueRedis
conn = None

def connect_db():
    global conn
    conn = pymysql.connect(host="172.16.16.15",port=3306,user="root",passwd="A1s1n0@zxyc#3",db="ixinnuo_sjcj",charset="utf8")
    return

def get_req_from_db():
    global conn
    cursor = conn.cursor()
    cursor.execute('select id, entname from req where status=0 order by id limit 10')
    results = cursor.fetchall()
    companies = []
    for res in results:
        company = {}
        company['id'] = res[0]
        company['name'] = res[1]
        companies.append(company)
    return companies

def main():
    my_queue = QueueRedis()
    result = my_queue.get_queue_length(settings.COMPANIES)
    print  result
    #mq 里存在数据则，3秒后退出
    if result:
        time.sleep(3)
        exit()
    time.sleep(3)
    global conn
    connect_db()
    source = get_req_from_db()
    for id_name in source:
        message = json.dumps(id_name)
        my_queue.send_to_queue(settings.COMPANIES, message)

    conn.close()
    print '成功添加队列%s条数据!!!' % len(source)

if __name__ == '__main__':
    main()


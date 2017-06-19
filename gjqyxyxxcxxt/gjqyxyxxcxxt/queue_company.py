# -*- coding: utf-8 -*-
import sys, os, json, time, pymongo
app_dir = os.path.abspath("../")
sys.path.append(app_dir)

from util.my_encode import Encoder
from gjqyxyxxcxxt import settings
from gjqyxyxxcxxt.database.my_mongo import Mongo
from gjqyxyxxcxxt.database.my_redis import QueueRedis

db = Mongo().get_db()
my_queue = QueueRedis()

result = my_queue.get_queue_length(settings.COMPANIES)
print  result
#mq 里存在数据则，3秒后退出
if result:
    time.sleep(3)
    exit()

list_crawl_where = {}

companies = list(db.ic_list.find(list_crawl_where).sort([("crawl_time", pymongo.ASCENDING)]).limit(1).skip(0))
if not companies:
    companies = list(db.ic_detail.find(list_crawl_where).sort([("crawl_time", pymongo.ASCENDING)]).limit(20).skip(0))
for company in companies:
    message = json.dumps(company, cls=Encoder)
    my_queue.send_to_queue(settings.COMPANIES, message)


#coding=utf-8
import sys
import os, json
#免去环境变量配置
app_dir = os.path.abspath("../")
sys.path.append(app_dir)

from database.my_redis import QueueRedis
from database.my_mongo import Mongo
from util.my_encode import Encoder

queue = QueueRedis()
mongo = Mongo()._get_db()
where = {'status': 0}
'''
results = list(mongo.ic_data_register.find(where))
print results
for result in results:
    result['status'] = 0
    message = json.dumps(result, cls=Encoder)
    queue.send_to_queue('regist_companies', message)
'''
results = list(mongo.ic_data_source.find(where))

for result in results:
    message = json.dumps(result, cls=Encoder)
    queue.send_to_queue('source_companies', message)
    break 

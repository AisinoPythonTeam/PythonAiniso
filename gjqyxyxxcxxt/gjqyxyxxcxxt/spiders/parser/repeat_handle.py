# -*- coding: utf-8 -*-
import hashlib
import json
import re
import time
from scrapy import log
from gjqyxyxxcxxt.database.my_redis import UniqRedis
class RepeatHandle(object):
    
    rdb = UniqRedis().conn()
    def repeat_query(self, url):
        key = hashlib.md5(url).hexdigest()
        return self.rdb.get(key)

    def add_to_redis(self, url):
        pipe = self.rdb.pipeline()
        pipe.set(hashlib.md5(url).hexdigest(), 1)
        result = pipe.execute()

    def set_value(self, company_hash, json_data):
        log.msg('_______res: %s' % json_data, level=log.WARNING)
        self.rdb.set(company_hash, json_data)

    def get_key(self, key):
        return self.rdb.get(key)

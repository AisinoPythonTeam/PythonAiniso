# -*- coding: utf-8 -*-
import redis, time
from gsgj_phone import settings
"""
    操作 redis的类
    """
class Singleton(object):
    
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class UniqRedis(Singleton):
    '''@ 此处采用单列模式，
       @ 避免过多的实例化。
        '''
    try:
        pool = redis.ConnectionPool(host=settings.UNIQ_REDIS_HOST, port = settings.UNIQ_REDIS_PORT)
        __db = redis.Redis(connection_pool=pool)
    except Exception, e:
        print e

    def conn(self):
        return self.__db

    def get_key(self, key):
        '''@ 去重，连接池方式，直接把key
           @ 搁置在顶层目录不妥
            '''
        return self.__db.get(key)

    def set_value(self, key, value):
        db = self.__db.set(key, value)

    """
    def count(self, key):
        '''@ 统计，连接池方式，连接较频繁，
           @ 下载量，真实下载量，重复数据量，解析失败数据量
           @ incr: 递增
            '''
        current_crawl_count = "%s%s_%s" % (settings.SERVER_FLAG, key, time.strftime("%Y_%m_%d_%H", time.localtime()))
        self.__db.incr(current_crawl_count)

    def get_count_result(self, key):
        '''@ 获取统计结果
           @ key: 需统计的key
            '''
        count = self.__db.get(key)
        print "%s: %s" % (key, count)
    """

class QueueRedis(Singleton):
    try:
        pool = redis.ConnectionPool(host=settings.QUEUE_REDIS_HOST, port=settings.QUEUE_REDIS_PORT)
        __db = redis.Redis(connection_pool=pool)
    except Exception, e:
        print e

    def read_from_queue(self, queueName, count):
        results = []
        for index in range(0, count):
            item = self.__dequeue(queueName)
            if item: results.append(item)
            else: return results
        return results

    def send_to_queue(self, queueName, message):
        self.__enqueue(queueName, message)

    def get_queue_length(self, queueName):
        return self.__db.llen(queueName)

    def __dequeue(self, queueName, block=False, timeout=3):
        """出队
            """
        try:
            if block:
                return self.__db.blpop(queueName, timeout=timeout)
            return self.__db.lpop(queueName)
        except Exception, e:
            print e
        return None

    def __enqueue(self, queueName, message):
        """入队
            """
        try:
            self.__db.rpush(queueName, message)
        except Exception, e:
            print e
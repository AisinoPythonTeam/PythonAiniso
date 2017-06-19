# -*- coding:utf-8 -*-
from pymongo import MongoClient
from gjqyxyxxcxxt import settings

"""
    操作 Mongo的类

"""
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class Mongo(Singleton):
    __conn = None
    __db = None

    def __init__(self, dbname = None):
        self.__db = self._get_db(dbname)

    #对外接口
    def get_db(self, dbname = None):
        return self.__db

    #私有方法
    def _get_db(self, dbname = None):
        if not self.__conn :
            self._get_conn()
        db = self.__conn.get_database('crawler')
        return db

    def _get_conn(self):
        host = settings.MONGO_HOST
        port = settings.MONGO_PORT
        user = settings.MONGO_AUTH_USER
        pwd = settings.MONGO_AUTH_PWD
        basename = 'admin'
        uri = 'mongodb://%s:%s@%s:%s/%s' % (user, pwd, host, port, basename)
        self.__conn = MongoClient(uri)

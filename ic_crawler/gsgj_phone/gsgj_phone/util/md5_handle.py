# -*- coding:utf-8 -*-
import hashlib

def get_md5_value(key):
    value = None
    try:
        value = hashlib.md5(key).hexdigest()
    except Exception, e:
        print e
    return value


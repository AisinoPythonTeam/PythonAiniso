# -*- coding:utf-8 -*-
import time
def get_current_date():
    currtime = time.localtime(time.time())
    date = time.strftime('%Y-%m-%d',currtime)
    timer = time.strftime('%H:%M:%S')
    T = date + " " + timer
    return T

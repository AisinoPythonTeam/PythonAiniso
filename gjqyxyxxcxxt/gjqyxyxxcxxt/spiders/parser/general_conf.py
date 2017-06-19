# -*- coding:utf-8 -*-
from gjqyxyxxcxxt.util._time import *
from gjqyxyxxcxxt.items import GjqyxyxxcxxtItem
def init_item():
    """
        初始化item
        """
    item = GjqyxyxxcxxtItem()
    for k in item.fields:
        item[k] = None
    item['CHGINFO'] = []
    item['PERINFO'] = []
    item['LEGINFO'] = []

    item['BRANINFO'] = []
    item['PARTNERCHAGEINFO'] = []
    item['CHGINFO'] = []
    item['MORTINFO'] = []
    item['EQUINFO'] = []
    item['FREEZEINFO'] = []
    item['LAWINFO'] = []
    item['EXCEINFO'] = []
    item['PUNINFO'] = []
    item['crawl_time'] = get_current_date()
    return item

def item_update(item_dic):
    item = init_item()
    for k in item.fields:
        if k in item_dic:
            item[k] = item_dic[k]
    return item

def base_info(key, company_name=''):
    detail_formdata ={
        'mobileAction': 'entDetail',
        'userID': 'id001',
        'userIP': '192.123.123.13'
    }
    czxx_formdata ={
        'mobileAction': 'invInfo',
        'userID': 'id001',
        'userIP': '192.123.123.13'
    }
    bgxx_formdata ={
        'mobileAction': 'altInfo',
        'startTime': '',
        'endTime': '',
        'userID': 'id001',
        'userIP': '192.123.123.13'
    }
    ryxx_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    search_formdata ={
        'mobileAction': 'entSearch',
        'keywords': u'%s' % company_name,
        'topic': '1',
        'pageNum': '1',
        'pageSize': '10',
        'userID': 'id001',
        'userIP': '192.123.123.13'
    }
    return eval(key)

# -*- coding:utf-8 -*-
def get_base_post_paramaters(key, company_name=''):
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
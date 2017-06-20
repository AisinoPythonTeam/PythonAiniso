# -*- coding:utf-8 -*-
from gsgj_phone.util.time_handler import *
from gsgj_phone.items import Item
def init_item():
    """
        初始化item
        """
    item = Item()
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
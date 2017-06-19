# -*- coding:utf-8 -*-
import re
from scrapy import log
from general_conf import *
class ParseHandle(object):
    def list_parse(self, companies):
        items = []
        short_name = None
        for company in companies:
            item = init_item()
            self.give_value(item, 'ENTNAME', 'ENTNAME', company)
            item['ENTNAME'], nouse = re.subn(u'<[^<>]+>', '', item['ENTNAME'])
            self.give_value(item, 'REGNO', 'REGNO', company)
            self.give_value(item, 'ESTDATE', 'ESTDATE', company)
            if isinstance(item['ESTDATE'], str) or isinstance(item['ESTDATE'], unicode):
                res = re.findall('\d{4}\D\d{1,2}\D\d{1,2}', item['ESTDATE'])
                if res:
                    item['ESTDATE'] = res[0]
            self.give_value(item, 'REGSTATE', 'REGSTATE_CN', company)
            short_name = item['ENTNAME'] if short_name is None or len(short_name) > len(item['ENTNAME']) else short_name
            ccp = {
                'pripid': str(company['PRIPID']).strip(),
                'enttype': str(company['ENTTYPE']).strip(),
                'nodenum': str(company['S_EXT_NODENUM']).strip()
            }
            item['detail_formdata'] = dict(base_info('detail_formdata'), **ccp)
            #item['czxx_formdata'] = dict(base_info('czxx_formdata'), **ccp)
            #item['ryxx_formdata'] = dict(base_info('ryxx_formdata'), **ccp)
            #item['bgxx_formdata'] = dict(base_info('bgxx_formdata'), **ccp)
            items.append(item)
        return items, short_name

    def detail_parse(self, item, res_json):
        
        self.give_value(item, 'UNISCID', 'UNISCID', res_json)
        self.give_value(item, 'ENTNAME', 'ENTNAME', res_json)
        self.give_value(item, 'ENTTYPE', 'ENTTYPE_CN', res_json)

        self.give_value(item, 'LEREP', 'NAME', res_json)
        self.give_value(item, 'REGCAP', 'REGCAP', res_json)
        self.give_value(item, 'ESTDATE', 'ESTDATE', res_json)
        self.give_value(item, 'OPFROM', 'OPFROM', res_json)
        self.give_value(item, 'OPTO', 'OPTO', res_json)
        self.give_value(item, 'REGORG', 'REGORG_CN', res_json)
        self.give_value(item, 'APPRDATE', 'APPRDATE', res_json)
        self.give_value(item, 'REGSTATE', 'REGSTATE', res_json)
        self.give_value(item, 'DOM', 'DOM', res_json)

        self.give_value(item, 'OPSCOPE', 'OPSCOPE', res_json)
        self.give_value(item, 'REGNO', 'REGNO', res_json)
        self.give_value(item, 'ORGAN_CODE', 'ORGAN_CODE', res_json)
        if item['REGCAP'] is None or not re.search('\d+', item['REGCAP']):
            item['REGCAP'] = None
        elif re.search(u'\d+[\u4e00-\u9fa5]+', item['REGCAP']):
            pass
        #else:
        #    item['REGCAP'] = item['REGCAP'] + '万元人民币'
        item['ID'] = item['REGNO']

    def czxx_parse(self, item, res_json):
        for dic in res_json:
            czxx_dic = {}
            czxx_dic['INV'] = ''
            czxx_dic['BLICTYPE'] = ''
            czxx_dic['FLAG'] = ''
            czxx_dic['INVDETAIL'] = ''
            czxx_dic['INVTYPE'] = ''
            czxx_dic['BLICNO'] = ''
            czxx_dic['ID'] = ''
            self.give_value(czxx_dic, 'INV', 'INVNAME', dic)
            self.give_value(czxx_dic, 'BLICTYPE', 'PAPERTYPE', dic)
            self.give_value(czxx_dic, 'FLAG', 'FLAG', dic)
            self.give_value(czxx_dic, 'INVTYPE', 'ENTTYPE_2', dic)
            self.give_value(czxx_dic, 'BLICNO', 'INVNO', dic)
            self.give_value(czxx_dic, 'ID', 'INVID', dic)
            czxx_dic['INVTYPE'] = '法人股东' if czxx_dic['INVTYPE'] == '1100' else '未定义'
            item['LEGINFO'].append(czxx_dic)

    def ryxx_parse(self, item, res_json):
        for dic in res_json:
            ryxx_dic = {}
            ryxx_dic['NAME'] = ''
            ryxx_dic['POSITION'] = ''
            self.give_value(ryxx_dic, 'NAME', 'NAME', dic)
            self.give_value(ryxx_dic, 'POSITION', 'POSITION_CN', dic)
            item['PERINFO'].append(ryxx_dic)

    def bgxx_parse(self, item, res_json):
        for dic in res_json:
            bgxx_dic = {}
            bgxx_dic['ALTITEM'] = ''
            bgxx_dic['ALTDATE'] = ''
            bgxx_dic['ALTBE'] = ''
            bgxx_dic['ALTAF'] = ''
            self.give_value(bgxx_dic, 'ALTITEM', 'ALTITEM_CN', dic)
            self.give_value(bgxx_dic, 'ALTDATE', 'ALTDATE', dic)
            self.give_value(bgxx_dic, 'ALTBE', 'ALTBE', dic)
            self.give_value(bgxx_dic, 'ALTAF', 'ALTAF', dic)
            item['CHGINFO'].append(bgxx_dic)

    def give_value(self, item, key, json_key, json_obj):
        if item[key]:
            return None

        res = json_obj.get(json_key, item[key])
        if not isinstance(res, unicode) and not isinstance(res, str):
            item[key] = ""
            return None

        item[key] = res.strip()

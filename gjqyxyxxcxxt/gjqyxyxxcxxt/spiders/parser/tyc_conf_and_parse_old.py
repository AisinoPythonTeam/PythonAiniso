# -*- coding:utf-8 -*-
import re, time
from gjqyxyxxcxxt.util._time import get_current_date
def get_url(key, param):
    url_dic = {
        'list_url': 'http://www.tianyancha.com/v2/search/%s.json?',
        'czxx_url': 'http://www.tianyancha.com/expanse/holder.json?id=%s&ps=100&pn=1',
        'ryxx_url': 'http://www.tianyancha.com/expanse/staff.json?id=%s&ps=100&pn=1',
        'xzcf_url': 'http://www.tianyancha.com/expanse/punishment.json?name=%s&ps=5&pn=1',
        'bgxx_url': 'http://www.tianyancha.com/expanse/changeinfo.json?id=%s&ps=100&pn=1',
        'ycxx_url': 'http://www.tianyancha.com/expanse/abnormal.json?id=%s&ps=10&pn=1',
        'fzjg_url': 'http://www.tianyancha.com/expanse/branch.json?id=%s&ps=10&pn=1'
    }
    return url_dic[key] % param

def get_conf(conf_name):
    referer_url = 'http://www.tianyancha.com/company/2313797533'
    sgArr = ["6","b","t","f","l", "5","w","h","q","i","s","e","c","p","m","u","9","8","y","2","z","k","j","r","x","n","-","0","3","4","d","1","a","o","7","v","g"]
    public_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    }
    my_headers = {
        "Tyc-From": "normal",
        "Accept": "application/json, text/plain, */*",
        "Referer": referer_url,
        "CheckError": "check",
        # "Accept-Encoding": "gzip, deflate, sdch",
        # "Accept-Language": "zh-CN,zh;q=0.8",
        # "Connection": "keep-alive",
        # "Host": "www.tianyancha.com",
        }
    return eval(conf_name)

def get_token_and_utm(tongji_page):
    js_code = "".join([chr(int(code)) for code in tongji_page.json()["data"]["v"].split(",")])
    token = re.findall(r"token=(\w+);", js_code)[0]
    fxck_chars = re.findall(r"\'([\d\,]+)\'", js_code)[0]
    four_count = fxck_chars.count('4')
    fxck_chars = fxck_chars.split(",")
    utm = ''
    for i in fxck_chars:
        if i == 4:
            if four_count > 1:
                utm += '2'
                continue
            else:
                utm += '1'
                continue
        if 5 < int(i) < 20:
            utm += get_conf('sgArr')[int(i)-2]
        else:
            utm += get_conf('sgArr')[int(i)]
    return token, utm

def html_clear(string):
    if not isinstance(string, str) and not isinstance(string, unicode):
        return string
    res, count = re.subn('<[^<>]+>', '', string)
    return  res

def time_format(dic, key):
    if dic[key]:
        res = re.findall('\d{4}\D\d{1,2}\D\d{1,2}', dic[key])
        if res:
            dic[key] = res[0]

def base_dic_init():
    base_info = {}
    base_info['ID'] = ''
    base_info['UNISCID'] = ''
    base_info['ENTTYPE'] = ''
    base_info['OPTO'] = ''
    base_info['REGORG'] = ''
    base_info['APPRDATE'] = ''
    base_info['REGNO'] = ''
    base_info['ORGAN_CODE'] = ''
    base_info['IXINNUOBM'] = ''
    base_info['industry'] = ''

    base_info['BRANINFO'] = []
    base_info['PARTNERCHAGEINFO'] = []
    base_info['MORTINFO'] = []
    base_info['EQUINFO'] = []
    base_info['FREEZEINFO'] = []
    base_info['LAWINFO'] = []
    base_info['EXCEINFO'] = []
    base_info['PUNINFO'] = []

    base_info['LEGINFO'] = []
    base_info['PERINFO'] = []
    base_info['CHGINFO'] = []

    return base_info

def base_info_parse(json_obj):
    base_info = base_dic_init()
    base_info['company_id'] = json_obj.get('id', None)
    base_info['websites'] = json_obj.get('websites', None)
    base_info['emails'] = json_obj.get('emails', None)
    base_info['province'] = json_obj.get('base', None)
    base_info['city'] = json_obj.get('city', None)
    base_info['crawl_time'] = get_current_date()

    base_info['OPSCOPE'] = json_obj.get('businessScope', None)
    base_info['DOM'] = json_obj.get('regLocation', None)
    base_info['OPFROM'] = json_obj.get('estiblishTime', None)
    base_info['ESTDATE'] = json_obj.get('estiblishTime', None)
    base_info['ENTNAME'] = json_obj.get('name', None)
    base_info['LEREP'] = json_obj.get('legalPersonName', None)
    base_info['REGCAP'] = json_obj.get('regCapital', None)
    base_info['REGSTATE'] = json_obj.get('regStatus', None)

    base_info['company_id'] = html_clear(base_info['company_id'])
    base_info['websites'] = html_clear(base_info['websites'])
    base_info['emails'] = html_clear(base_info['emails'])
    base_info['province'] = html_clear(base_info['province'])
    base_info['city'] = html_clear(base_info['city'])

    base_info['OPSCOPE'] = html_clear(base_info['OPSCOPE'])
    base_info['DOM'] = html_clear(base_info['DOM'])
    base_info['OPFROM'] = html_clear(base_info['OPFROM'])
    base_info['ESTDATE'] = html_clear(base_info['ESTDATE'])
    base_info['ENTNAME'] = html_clear(base_info['ENTNAME'])
    base_info['LEREP'] = html_clear(base_info['LEREP'])
    base_info['REGCAP'] = html_clear(base_info['REGCAP'])
    base_info['REGSTATE'] = html_clear(base_info['REGSTATE'])

    time_format(base_info, 'ESTDATE')
    time_format(base_info, 'OPTO')
    time_format(base_info, 'OPFROM')
    time_format(base_info, 'APPRDATE')

    return base_info

def czxx_parse(json_obj):
    LEGINFO = []
    for obj in json_obj['data']['result']:
        czxx_dic = {}
        czxx_dic['BLICTYPE'] = ''
        czxx_dic['FLAG'] = ''
        czxx_dic['INVTYPE'] = ''
        czxx_dic['BLICNO'] = ''
        czxx_dic['INV'] = obj.get('name', None)
        czxx_dic['ID'] = obj.get('id', None)
        czxx_dic['INV'] = html_clear(czxx_dic['INV'])
        czxx_dic['ID'] = html_clear(czxx_dic['ID'])

        my_dic = {}
        my_dic['INV'] = obj.get('name', None)
        my_dic['LISUBCONAM'] = None
        my_dic['LIACCONAM'] = None
        my_dic['PAYINFO'] = []
        my_dic['REALPAYINFO'] = []
        print '====>>>: ', obj['capitalActl']
        if 'capital' in obj and obj['capital']:
            for payinfo in obj['capital']:
                pay_dic = {}
                pay_dic['CONDATE'] = payinfo.get('time', None)
                pay_dic['CONFORM'] = payinfo.get('paymet', None)
                pay_dic['SUBCONAM'] = payinfo.get('amomon', None)
                pay_dic['CONFORM'] = html_clear(pay_dic['CONFORM'])
                pay_dic['SUBCONAM'] = html_clear(pay_dic['SUBCONAM'])
                pay_dic['CONDATE'] = html_clear(pay_dic['CONDATE'])
                my_dic['PAYINFO'].append(pay_dic)
        if 'capitalActl' in obj and obj['capitalActl']:
            for readpayinfo in obj['capitalActl']:
                real_pay_dic = {}
                real_pay_dic['CONDATE'] = readpayinfo.get('time', None)
                real_pay_dic['CONFORM'] = readpayinfo.get('paymet', None)
                real_pay_dic['SUBCONAM'] = readpayinfo.get('amomon', None)
                real_pay_dic['CONFORM'] = html_clear(real_pay_dic['CONFORM'])
                real_pay_dic['SUBCONAM'] = html_clear(real_pay_dic['SUBCONAM'])
                real_pay_dic['CONDATE'] = html_clear(real_pay_dic['CONDATE'])
                my_dic['REALPAYINFO'].append(real_pay_dic)
        czxx_dic['INVDETAIL'] = my_dic
        LEGINFO.append(czxx_dic)

    return 'LEGINFO', LEGINFO

def ryxx_parse(json_obj):
    PERINFO = []
    for obj in json_obj['data']['result']:
        ryxx_dic = {}
        ryxx_dic['NAME'] = obj.get('name', None)
        typeJoin = obj.get('typeJoin', None)
        ryxx_dic['POSITION'] = ', '.join(typeJoin) if isinstance(typeJoin, list) else typeJoin
        ryxx_dic['NAME'] = html_clear(ryxx_dic['NAME'])
        ryxx_dic['POSITION'] = html_clear(ryxx_dic['POSITION'])
        PERINFO.append(ryxx_dic)

    return 'PERINFO', PERINFO

def xzcf_parse(json_obj):
    PUNINFO = []
    for dic_obj in json_obj['data']['items']:
        dic = {}
        dic['PENDECNO'] = dic_obj.get('punishNumber', None)
        dic['ILLEGACTTYPE'] = dic_obj.get('type', None)

        dic['PENTYPE'] = dic_obj.get('PENTYPE', None)
        dic['PENAM'] = dic_obj.get('PENAM', None)
        dic['FORFAM'] = dic_obj.get('FORFAM', None)

        dic['content'] = dic_obj.get('content', None)
        dic['decisionDate'] = dic_obj.get('decisionDate', None)
        dic['PENAUTH'] = dic_obj.get('departmentName', None)
        dic['PENDECISSDATE'] = dic_obj.get('publishDate', None)
        PUNINFO.append(dic)
    return 'PUNINFO', PUNINFO

def bgxx_parse(json_obj):
    CHGINFO = []
    for obj in json_obj['data']['result']:
        bgxx_dic = {}
        bgxx_dic['ALTITEM'] = obj.get('changeItem', None)
        bgxx_dic['ALTITEM'] = html_clear(bgxx_dic['ALTITEM'])
        bgxx_dic['ALTDATE'] = obj.get('changeTime', None)
        bgxx_dic['ALTDATE'] = html_clear(bgxx_dic['ALTDATE'])
        time_format(bgxx_dic, 'ALTDATE')
        bgxx_dic['ALTBE'] = obj.get('contentBefore', None)
        bgxx_dic['ALTBE'] = html_clear(bgxx_dic['ALTBE'])
        if bgxx_dic['ALTBE']:
            bgxx_dic['ALTBE'], c = re.subn(ur'[A-Za-z\r\n]+', '', bgxx_dic['ALTBE'])
        bgxx_dic['ALTAF'] = obj.get('contentAfter', None)
        bgxx_dic['ALTAF'] = html_clear(bgxx_dic['ALTAF'])
        if bgxx_dic['ALTAF']:
            bgxx_dic['ALTAF'], c = re.subn(ur'[A-Za-z\r\n]+', '', bgxx_dic['ALTAF'])
        CHGINFO.append(bgxx_dic)
    return 'CHGINFO', CHGINFO

def ycxx_parse(json_obj):
    EXCEINFO = []
    for obj in json_obj['data']['result']:
        fzjg_dic = {}
        fzjg_dic['SPECAUSE'] = obj.get('putReason', None)
        fzjg_dic['ABNTIME'] = obj.get('putDate', None)
        fzjg_dic['DECORG'] = obj.get('putDepartment', None)
        EXCEINFO.append(fzjg_dic)
    return 'EXCEINFO', EXCEINFO

def fzjg_parse(json_obj):
    BRANINFO = []
    for obj in json_obj['data']['result']:
        fzjg_dic = {}
        fzjg_dic['BRNAME'] = obj.get('name', None)
        fzjg_dic['LEREP'] = obj.get('legalPersonName', None)
        fzjg_dic['REGSTATE'] = obj.get('regStatus', None)
        fzjg_dic['ESTDATE'] = obj.get('estiblishTime', None)
        if fzjg_dic['ESTDATE']:
            timestamp = int(str(fzjg_dic['ESTDATE'])[:10])
            fzjg_dic['ESTDATE'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

        fzjg_dic['REGNO'] = obj.get('REGNO', None)
        fzjg_dic['DOM'] = obj.get('DOM', None)
        fzjg_dic['REGORG'] = obj.get('REGORG', None)
        fzjg_dic['UNISCID'] = obj.get('UNISCID', None)
        fzjg_dic['TEL'] = obj.get('TEL', None)
        fzjg_dic['ADDR'] = obj.get('ADDR', None)

        fzjg_dic['regCapital'] = obj.get('regCapital', None)
        fzjg_dic['category'] = obj.get('category', None)
        BRANINFO.append(fzjg_dic)
    return 'BRANINFO', BRANINFO


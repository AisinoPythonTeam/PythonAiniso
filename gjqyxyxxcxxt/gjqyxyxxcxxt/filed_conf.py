# -*- coding:utf-8 -*-
import time, re

base_keys = [
    'UNISCID', 
    'ENTNAME', 
    'ENTTYPE', 
    'LEREP', 
    'REGCAP',
    'ESTDATE', 
    'OPFROM', 
    'OPTO', 
    'REGORG', 
    'APPRDATE',
    'REGSTATE', 
    'DOM', 
    'OPSCOPE', 
    'REGNO', 
    'ORGAN_CODE',
    'IXINNUOBM', 
    'ID'
]

other_keys = [
    'LEGINFO', 
    'PERINFO', 
    'CHGINFO', 
    'BRANINFO', 
    'PARTNERCHAGEINFO',
    'MORTINFO', 
    'EQUINFO', 
    'FREEZEINFO', 
    'LAWINFO', 
    'EXCEINFO',
    'PUNINFO'
]

def get_value(obj):
    return obj

def init_handle():
    json_data = {}
    json_data['abstract'] = ''
    json_data['errNum'] = 0
    json_data['userID'] = ''
    json_data['errMsg'] = 'success'
    json_data['timeStamps'] = time.time() * 1000
    retData = {}
    for key in base_keys:
        retData[key] = None
    for key in other_keys:
        retData[key] = []
    json_data['retData'] = retData
    return json_data

#mysql_____________________________________________
def get_info_from_mysql(cursor, data):
    sql = 'SELECT ENTNAME, GSZCH, UNISCID, ENTTYPE, LEREP, REGCAP, ESTDATE, DOM, OPFROM, OPTO, REGORG, APPRDATE, REGSTATE, OPSCOPE FROM gsxt_data WHERE ENTNAME=\'%s\'' % data['company_name']
    cursor.execute(sql)
    base_results = cursor.fetchall()
    if base_results:
        data['status'] = 1
        data['data_source'] = 'mysql_db'
        mysql_give_value(base_results, data)

        czxx_sql = 'SELECT `股东名称`, `股东类型`, `证照/证件类型`, `证照/证件号码` FROM gsxt_gdxx WHERE 公司名称= \'%s\'' % data['company_name']
        cursor.execute(czxx_sql)
        czxx_results = cursor.fetchall()
        if czxx_results:
            mysql_give_gdxx_value(czxx_results, data)

        ryxx_sql = 'SELECT `职位`, `姓名` FROM gsxt_ryxx WHERE 公司名称= \'%s\'' % data['company_name']
        cursor.execute(ryxx_sql)
        ryxx_results = cursor.fetchall()
        if ryxx_results:
            mysql_give_ryxx_value(ryxx_results, data)

        bgxx_sql = 'SELECT `变更事项`, `变更前内容`, `变更后内容`, `变更日期` FROM gsxt_bgxx WHERE 公司名称= \'%s\'' % data['company_name']
        cursor.execute(bgxx_sql)
        bgxx_results = cursor.fetchall()
        if bgxx_results:
            mysql_give_bgxx_value(bgxx_results, data)

def mysql_give_value(base_results, data):
    mysql_keys = ['ENTNAME', 'REGNO', 'UNISCID', 'ENTTYPE', 'LEREP', 'REGCAP',
    'ESTDATE', 'DOM', 'OPFROM', 'OPTO', 'REGORG', 'APPRDATE', 'REGSTATE', 'OPSCOPE']

    ENTNAME, REGNO, UNISCID, ENTTYPE, LEREP, REGCAP, ESTDATE, DOM, OPFROM, OPTO, REGORG, APPRDATE, REGSTATE, OPSCOPE = base_results[0]
    for k in mysql_keys:
        curr_v = data['json_data']['retData'][k]
        data['json_data']['retData'][k] = eval(k) if (not curr_v or len(curr_v) < 4) else curr_v

def mysql_give_gdxx_value(czxx_results, data):
    #股东及出资信息处理
    if not czxx_results:
        return
    czxx = []
    for obj in czxx_results:
        czxx_dic = {}
        czxx_dic['INV'], c = re.subn('[\{\}]*', '', obj[0])
        czxx_dic['INVTYPE'], c = re.subn('[\{\}]*', '', obj[1])
        czxx_dic['BLICTYPE'], c = re.subn('[\{\}]*', '', obj[2])
        czxx_dic['BLICNO'], c = re.subn('[\{\}]*', '', obj[3])
        czxx_dic['ID'] = ''
        czxx.append(czxx_dic)
    data['json_data']['retData']['LEGINFO'] = czxx

def mysql_give_ryxx_value(ryxx_results, data):
    ryxx = []
    for obj in ryxx_results:
        ryxx_dic = {}
        ryxx_dic['NAME'] = obj[1]
        ryxx_dic['POSITION'] = obj[0]
        ryxx.append(ryxx_dic)
    data['json_data']['retData']['PERINFO'] = ryxx_dic

def mysql_give_bgxx_value(bgxx_results, data):
    bgxx = []
    for obj in bgxx_results:
        bgxx_dic = {}
        bgxx_dic['ALTITEM'] = obj[0]
        bgxx_dic['ALTBE'] = obj[1]
        bgxx_dic['ALTAF'] = obj[2]
        bgxx_dic['ALTDATE'] = obj[3]


def add_company_name_to_req(conn, company_name):
    req_sql = 'INSERT INTO req (ENTNAME, STATUS) VALUES (\'%s\', \'%s\')' % (company_name, 0)
    cursor = conn.cursor()
    cursor.execute(req_sql)
    conn.commit()

def add_base_info_to_mysql(conn, retData):
    #base_info
    b_sql = 'INSERT INTO gsxt_data(ENTNAME, GSZCH, UNISCID, ENTTYPE, LEREP, REGCAP, ESTDATE, DOM, OPFROM, OPTO, REGORG, APPRDATE, REGSTATE, CREATETIME, OPSCOPE) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (
                            retData['ENTNAME'], retData['REGNO'], retData['UNISCID'], retData['ENTTYPE'], retData['LEREP'],
                            (retData['REGCAP']), retData['ESTDATE'], retData['DOM'], retData['OPFROM'], retData['OPTO'],
                            retData['REGORG'], retData['APPRDATE'], retData['REGSTATE'], retData['crawl_time'], retData['OPSCOPE'])
    cursor = conn.cursor()
    cursor.execute(b_sql)
    conn.commit()

def add_ryxx_to_mysql(conn, retData):
    for ryxx in retData['PERINFO']:
        r_sql = 'INSERT INTO gsxt_ryxx (公司名称, 姓名, 职位) VALUES (\'%s\', \'%s\', \'%s\')' % \
            (retData['ENTNAME'].encode('utf-8') if retData['ENTNAME'] else retData['ENTNAME'], 
                ryxx['NAME'].encode('utf-8') if ryxx['NAME'] else ryxx['NAME'],
                ryxx['POSITION'].encode('utf-8') if ryxx['POSITION'] else ryxx['POSITION'])
    cursor = conn.cursor()
    cursor.execute(r_sql)
    conn.commit()

def add_bgxx_to_mysql(conn, retData):
    for bgxx in retData['CHGINFO']:
        bg_sql = 'INSERT INTO gsxt_bgxx (公司名称, 变更事项, 变更前内容, 变更后内容, 变更日期) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % \
                    (retData['ENTNAME'].encode('utf-8') if retData['ENTNAME'] else retData['ENTNAME'],
                    bgxx['ALTITEM'].encode('utf-8') if bgxx['ALTITEM'] else bgxx['ALTITEM'],
                    bgxx['ALTBE'].encode('utf-8') if bgxx['ALTBE'] else bgxx['ALTBE'],
                    bgxx['ALTAF'].encode('utf-8') if bgxx['ALTAF'] else bgxx['ALTAF'],
                    bgxx['ALTDATE'].encode('utf-8') if bgxx['ALTDATE'] else bgxx['ALTDATE'])
    cursor = conn.cursor()
    cursor.execute(bg_sql)
    conn.commit()

def add_czxx_to_mysql(conn, retData):
    for czxx in retData['LEGINFO']:
        czxx_sql = 'INSERT INTO gsxt_gdxx (公司名称, 股东名称, 股东类型, `证照/证件类型`, `证照/证件号码`, 详情) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (
            retData['ENTNAME'], czxx['INV'],'自然人股东',czxx['BLICTYPE'],czxx['BLICNO'],"")
    cursor = conn.cursor()
    cursor.execute(czxx_sql)
    conn.commit()
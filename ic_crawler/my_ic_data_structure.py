#coding=utf-8
base_fields = {
    "TEL":"",           #(01)电话
    "EMAIL":"",         #(02)邮箱
    "SITE":"",          #(03)网址
    "ENTNAME":"",      #(04)企业名称
    "REGNO":"",         #(05)工商注册号
    "ORGAN_CODE":"",    #(06)组织机构代码
    "NSRSBH":"",        #(07)纳税人识别号
    "UNISCID":"",       #(08)统一信用代码
    "LEREP":"",         #(09)法定代表人
    "ENTTYPE":"",        #(10)类型
    "TRADE":"",         #(11)行业
    "REGCAP":"",        #(12)注册资本
    "ESTDATE":"",       #(13)成立日期
    "OPFROM":"",        #(14)经营期限自
    "OPTO":"",          #(15)经营期限至
    "REGORG":"",        #(16)登记机关
    "APPRDATE":"",      #(17)核准日期
    "DOM":"",           #(18)住所
    "REGSTATE":"",      #(19)登记状态
    "OPSCOPE":"",       #(20)经营范围
    "AMBO":"",          #(21)股票代码
    "LOGO":"",          #(22)logo图片
    "SHARESTYPE":"",    #(23)股票种类
    "SHORTNAME":"",     #(24)公司简称
    "PROVINCE":"",      #(25)所在省份
    "CITY":"",          #(26)所在城市
}
null_fields = {
    "TEL":"",           #(01)电话
    "EMAIL":"",         #(02)邮箱
    "SITE":"",          #(03)网址
    "ENTNAME":"",       #(04)企业名称
    "REGNO":"",         #(05)工商注册号
    "ORGAN_CODE":"",    #(06)组织机构代码
    "NSRSBH":"",        #(07)纳税人识别号
    "UNISCID":"",       #(08)统一信用代码
    "LEREP":"",         #(09)法定代表人
    "ENTTYPE":"",       #(10)类型
    "TRADE":"",         #(11)行业
    "REGCAP":"",        #(12)注册资本
    "ESTDATE":"",       #(13)成立日期
    "OPFROM":"",        #(14)经营期限自
    "OPTO":"",          #(15)经营期限至
    "REGORG":"",        #(16)登记机关
    "APPRDATE":"",      #(17)核准日期
    "DOM":"",           #(18)住所
    "REGSTATE":"",      #(19)登记状态
    "OPSCOPE":"",       #(20)经营范围
    "AMBO":"",          #(21)股票代码
    "LOGO":"",          #(22)logo图片
    "SHARESTYPE":"",    #(23)股票种类
    "SHORTNAME":"",     #(24)公司简称
    "PROVINCE":"",      #(25)所在省份
    "CITY":"",          #(26)所在城市

    "LEGINFO": [],      #2股东信息
    "PERINFO": [],      #3主要人员信息
    "BRANINFO": [],     #4分支机构
    "CHGINFO": [],      #5变更信息
    "PUNINFO": [],      #6行政处罚
    "EXCEINFO": [],     #7经营异常
    "EQUINFO": [],      #8股权出质
    "MORTINFO": [],     #9动产抵押

    "QYGX":[],          #10企业关系
    "QYNB":[],          #11企业年报
    "INVEST":[],        #12对外投资
    "FLSS":[],          #13法律诉讼
    "FYGG":[],          #14法院公告
    "SXR":[],           #15失信人
    "BZXR":[],          #16被执行人

    "LAWINFO": [],      #17严重违法
    "TOWNTAX":[],       #18欠税公告
    "TMINFO":[],        #19商标信息
    "PATENT":[],        #20专利
    "COPYRIGHT":[],     #21著作权

    "WZBA":[],          #22网站备案
    "RZLS":[],          #23融资历史
    "HXTD":[],          #24核心团队
    "QYYW":[],          #25企业业务
    "TZSJ":[],          #26投资事件
    "JPXX":[],          #27竞品信息
    "ZTB":[],           #28招投标
    "ZQXX":[],          #29债券信息
    "GDXX":[],          #30购地信息
    "ZPXX":[],          #31招聘信息
    "SWPJ":[],          #32税务评级
    "CCJC":[],          #33抽查检查
    "CPXX":[],          #34产品信息
    "ZZZS":[],          #35资质证书
    "FREEZEINFO": [],   #36股权冻结信息

    #司法部分____________________________
    "sxgg": [],         #37失信公告
    "cpws": [],         #38裁判文书
    "zdsswf": [],       #39重大税收违法案件
    "zfcgwf":[]         #40政府采购严重违法失信信息
}

#2股东信息
LEGINFO =  {
    "ID": "",       #唯一标示
    "BLICNO": "",   #证照编号
    "BLICTYPE": "", #证照类型
    "INV": "",  #主管部门名称/股东/发起人名称
    "INVTYPE": "",  #主管部门类型/股东/发起人类型
    "INVDETAIL": {}
}

#INVDETAIL
INVDETAIL = {
        "INV":"",   #主管部门名称/股东/发起人名称
        "LISUBCONAM":"", #累计认缴额
        "LIACCONAM":"",  #累计实缴额
        "PUBDATE":"",    #公示日期
        "CZRATIO":"",    #出资比例
        "PAYINFO": [],
        "REALPAYINFO":[],
}

#PAYINFO
PAYINFO = {
    "CONFORM":"",   #认缴出资方式
    "SUBCONAM":"",  #认缴出资额
    "CONDATE":"",   #认缴出资日期
}
REALPAYINFO = {
    "CONFORM":"",   #实缴出资方式
    "ACCONAM":"",   #实缴出资额
    "CONDATE":"",   #实缴出资日期
}

#3主要人员信息
PERINFO = {
    "NAME":"",      #姓名
    "POSITION":""   #职位
}

#4分支机构
BRANINFO =  {
    "BRNAME":"",   #名称
    "LEREP":"",     #法定代表人
    "REGSTATE":"",  #登记状态
    "ESTDATE":"",   #成立日期
    "REGNO":"",     #注册号
    "REGORG":"",    #登记机关
    "UNISCID":"",   #统一社会信用代码
    "TEL":"",       #联系电话
    "ADDR":"",      #通信地址
    "DOM":""        #住所
}
#5变更信息
CHGINFO = {
    "ALTITEM":"",  #变更事项
    "ALTDATE":"",   #变更日期
    "ALTBE":"",     #变更前内容
    "ALTAF":""      #变更后内容
}

#6行政处罚
PUNINFO = {
    "PENDECNO":"",  #处罚决定书文号
    "ILLEGACTTYPE":"", #违法行为类型
    "PENTYPE":"",   #处罚种类
    "PENAM":"", #罚款金额
    "FORFAM":"",    #没收金额
    "PENAUTH":"",   #作出行政处罚决定机关名称
    "PENDECISSDATE":"", #作出处罚决定书日期
    "LEREP":"", #法定代表人(负责人)姓名
    "REMARK":"" #备注
}

#7经营异常
EXCEINFO = {
    "SPECAUSE":"",  #列入经营异常名录原因
    "ABNTIME":"",   #列入日期
    "REMEXCPRES":"",#移出经营异常名录
    "REMDATE":"",   #移出日期
    "DECORG":"",    #作出决定机关
    "YCCAUSE":"",   #移除原因
    "YCORG":""      #移除机关
}
#8股权出质
EQUINFO = {
    "EQUPLEDATE":"",    #股权出质登记日期
    "EQUITYNO":"",  #股权登记编号
    "TYPE":"", #状态
    "IMPAM":"", #出质股权数额
    "REGCAPCUR":"", #出质股权数额币种
    "PLEDAMUNIT":"",    #出质股权数额单位
    "PLEDGOR":"",   #出质人
    "PLEDNO":"",    #出质人证照号码（添加）
    "IMPORG":"",    #质权人
    "BLICNO":"",   #质权人证照号码
    "BLICTYPE":"",  #质权人证照类型
    "REMARK":""     #备注
}
#9动产抵押
MORTINFO = {
    "MORREGCNO":"",     #动产抵押登记编号
    "REGIDATE":"",      #登记日期
    "REGORG":"",        #登记机关
    "TYPE":"",          #状态
    "PRICLASECKIND":"", #被担保债权种类
    "PRICLASECAM":"",   #被担保债权数额
    "REGCAPCUR":"",     #被担保债权数额币种
    "PEFPERFORM":"",    #债务人履行债务的期限自
    "PEFPERTO":"",      #债务人履行债务的期限至
    "WARCOV":"",        #担保范围
    "REMARK":"",        #备注
    "DYQRMC":"",        #抵押权人名称
    "DYQRZJ":"",        #抵押权人证照／证件类型
    "ZJHM":"",          #证件／证照号码
    "ZSD":"",           #住所地
    "DYWMC":"",         #抵押物名称
    "SYQGS":"",         #所有权或使用权归属
    "GSQK":"",          #数量、质量、状况、所在地等情况
    "DYWBZ":""          #(抵押物)备注
}
#17严重违法
LAWINFO = {
    "SERILLREA":"", #列入严重违法企业名单原因
    "ABNTIME":"",   #列入日期
    "REMDATE":"",   #移出日期
    "REMEXCPRES":"",#移出严重违法企业名单原因
    "DECORG":"",  #作出决定机关
}
#36股权冻结信息
FREEZEINFO = {
    "BEEXECUTED":"",    #被执行人
    "EXECUTEDAM":"",    #股权数额
    "COURTDEPT":"",     #执行法院
    "REFERENCENUM":"",  #协助公示通知书文号
    "PUBDATE":"",       #公示日期
    "FREEZEFROM":"",    #冻结期限自
    "FREEZETO":"",      #冻结期限至
}

#对外投资
INVEST = {
    "EXT_COMPANY_NAME":"", #被投资企业名称
    "EXT_LEREP":"",        #被投资企业法人
    "CAPITAL":"",          #注册资本
    "AMOUNT":"",           #投资数额
    "RATIO":"",            #投资比例
    "REGDATE":"",          #注册时间
    "STATUS":"",           #状态
}

#欠税公告
TOWNTAX = {
    "PUB_DATE":"",      #发布日期
    "NSRSBH":"",        #纳税人识别号
    "TYPE":"",          #欠税税种
    "OW_AMOUNT":"",     #当前发生的欠税额
    "OW_REMAIN":"",     #欠税余额
    "TAX_AUTHORITY":"", #税务机关
}

#商标信息
TMINFO = {
    "APP_DATE":"",      #申请日期
    "TM_LOGO":"",       #商标
    "TM_NAME":"",       #商标名称
    "REGNO":"",         #注册号
    "TYPE":"",          #类别
    "STATUS":"",        #状态
}

#专利信息
PATENT = {
    "APP_PUB_NUM":"",      #申请公布号
    "APP_NO":"",           #申请号
    "CLSFYNO":"",          #分类号
    "IMG_URL":"",          #图片地址
    "PATENT_NAME":"",      #专利/发明名称
    "ADDRESS":"",          #地址
    "INVENTOR":"",         #发明人
    "APPLICANT_NAME":"",   #申请人
    "APP_DATE":"",         #申请日期
    "APP_PUB_DATE":"",     #申请公布日
    "AGENCY":"",           #代理机构
    "AGENT":"",            #代理人
    "ABSTRACTS":""         #摘要
}

#著作权
COPYRIGHT = {
    "REGTIME":"",           #批准日期/登记日期
    "FULLNAME":"",          #软件全称
    "NAME":"",              #软件简称
    "REGNUM":"",            #登记号
    "CATNUM":"",            #分类号
    "VERSION":"",           #版本号
    "AUTHOR_NATIONALITY":"",#著作权人(国籍)"
    "PUBLISHTIME":""        #首次发表日期
}



#司法部分
#____________________________________________________________
#失信公告
sxgg = {
    "md5_source":   "rowkey来源",
    "md5":          "rowkey",
    "frfzr":        "法定代表人或者负责人姓名",
    "age":          "年龄",
    "sex":          "性别",
    "body":         "全部内容",
    "lxqk":         "被执行人的履行情况",
    "yiwu":         "生效法律文书确定的义务",
    "court":        "执行法院",
    "yjdw":         "做出执行依据单位",
    "sortTime":     "立案时间时间戳", 
    "province":     "省份",
    "sortTimeString": "立案时间",
    "jtqx":         "失信被执行人行为具体情形",
    "pname":        "被执行人姓名/名称",
    "postTime":     "发布时间",
    "yjCode":       "执行依据文号",
    "sxggId":       "法海自定义id",
    "caseNo":       "案号",
    "idcardNo":     "身份证号码/组织机构代码",
    "ylx":          "已履行部分",
    "wlx":          "未履行部分",
    "datafrom":     "数据来源",
    "dataType":     "sxgg"
}

#裁判文书
cpws = {
    "md5_source":       "rowkey来源",
    "md5":              "rowkey",
    "body":             "内容",
    "partys": [{
        "status":       "当事人立场 （p上诉人, d被上诉人,t第三人）",
        "title":        "当事人称号",
        "lawOffice":    "律师事务所",
        "birthday":     "当事人生日",
        "pname":        "当事人名称",
        "lawyer":       "委托辩护人",
        "address":      "当事人住所地", 
        "idcardNo":     "当事人身份证号",
        "partyType":    "当事人类型"}],
    "court":            "法院名称",
    "sortTime":         "审结时间",
    "title":            "标题",
    "caseCause":        "案由",
    "judgeResult":      "判决结果", 
    "trialProcedure":   "审理程序",
    "cpwsId":           "法海自定义id",
    "judge":            "审判员",
    "caseType":         "文书类型",
    "caseNo":           "案号",
    "yiju":             "依据法律条文",
    "dataType":         "cpws",
    "courtRank":        "未知",
    "anyou":            "未知",
    "anyouType":        "未知",
}

#重大税收违法案件当事人名单字段
zdsswf = {
    "md5_source":       "rowkey来源",
    "md5":              "rowkey",
    "datafrom":         "数据来源",
    "data_type":        "数据类别",
    "pname":            "纳税人名称",
    "NSRSBH":           "纳税人识别码",
    "ORGAN_CODE":       "组织机构代码",
    "DOM":              "注册地址",
    "LEREP":            "法定代表人或者负责人姓名",
    "LEREP_sex":        "法定代表人或者负责人性别",
    "LEREP_zjmc":       "法定代表人或者负责人证件名称",
    "cwfzr":            "负有直接责任的财务负责人姓名",
    "cwfzr_sex":        "负有直接责任的财务负责人性别",
    "cwfzr_zjmc":       "负有直接责任的财务负责人证件名称",
    "zjjg":             "负有直接责任的中介机构信息及其从业人员信息",
    "ajxz":             "案件性质",
    "wfss":             "主要违法事实",
    "yijujcf":          "相关法律依据及税务处理处罚情况",
    "sbdate":           "案件上报期",
    "update_date":      "最新更新日期"
    }

#政府采购严重违法失信信息
zfcgwf = {
    "md5_source":       "rowkey来源",
    "md5":              "rowkey",
    "datafrom":         "数据来源",
    "data_type":        "数据类别",
    "gysmc":            "供应商或代理机构名称",
    "address":          "地址",
    "jtqx":             "不良行为的具体情形",
    "cfjg":             "处罚结果",
    "yiju":             "处罚依据",
    "cf_date":          "处罚（记录）日期",
    "zfdw":             "执法（记录）单位",
    "js_date":          "处罚结束时间",
    "update_date":      "最新更新日期"
    }
#coding=utf-8

data_structure = {
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

    #2股东信息
    "LEGINFO": {
        "operation":"replace",
        "data_type":"gs_V1",
        "data": []
    },
    #3主要人员信息
    "PERINFO": {
        "operation":"replace",
        "data_type":"gs_V1",
        "data": []
    },
    #4分支机构
    "BRANINFO": {
        "operation":"append",
        "data_type":"gs_V1",
        "data": []
    },
    #5变更信息
    "CHGINFO": {
        "operation":"append",
        "data_type":"gs_V1",
        "data": []
    },
    #6行政处罚
    "PUNINFO": {
        "operation":"append",
        "data_type":"gs_V1",
        "data": []
    },
    #7经营异常
    "EXCEINFO": {
        "operation":"append",
        "data_type":"gs_V1",
        "data": []
    },
    #8股权出质
    "EQUINFO": {
        "operation":"append",
        "data_type":"gs_V1",
        "data": []
    },
    #9动产抵押
    "MORTINFO": {
        "operation":"append",
        "data_type":"gs_V1",
        "data": []
    },
    #12对外投资
    "INVEST": {
        "operation":"append",
        "data_type":"gs_V1",
        "data": []
    },
    #17严重违法
    "LAWINFO": {
        "operation":"append",
        "data_type":"gs_V1",
        "data": []
    },
    #欠税公告
    "TOWNTAX": {
        "operation":"append",
        "data_type":"gs_V1",
        "data": []
    },
    #商标信息
    "TMINFO": {
        "operation":"append",
        "data_type":"gs_V1",
        "data": []
    },
    #专利
    "PATENT": {
        "operation":"append",
        "data_type":"gs_V1",
        "data": []
    },
    #著作权
    "COPYRIGHT": {
        "operation":"append",
        "data_type":"gs_V1",
        "data": []
    },
    #股权冻结信息
    "FREEZEINFO": {
        "operation":"append",
        "data_type":"gs_V1",
        "data": []
    },

# V3新增_________________________________
    #网站备案
    "websiteRecode":{
        "operation":"append",
        "data_type":"gs",
        "data": []
    },
    #招投标
    "bidding": {
        "operation":"append",
        "data_type":"gs",
        "data": []
    },
    #债券信息
    "bondInfo": {
        "operation":"append",
        "data_type":"gs",
        "data": []
    },
    #税务评级
    "taxRating": {
        "operation":"append",
        "data_type":"gs",
        "data": []
    },
    #资质证书
    "qualificationCertificate": {
        "operation":"append",
        "data_type":"gs",
        "data": []
    },
    #抽查检查
    "spotCheck": {
        "operation":"append",
        "data_type":"gs",
        "data": []
    },
    #产品信息
    "productInfo": {
        "operation":"append",
        "data_type":"gs",
        "data": []
    },
    #进出口信用
    "impExpCredit": {
        "operation":"append",
        "data_type":"gs",
        "data": []
    },
    #企业关系
    "companyRelationship": {
        "operation":"replace",
        "data_type":"gs",
        "data": []
    },



#信用中国部分—————————————————————————————
    #失信公告
    "sxgg": {
        "operation":"append",
        "data_type":"gs",
        "data": []
    },
    #重大税收违法案件
    "zdsswf": {
        "operation":"append",
        "data_type":"sw",
        "data": []
    },
    #政府采购严重违法失信信息
    "zfcgwf": {
        "operation":"append",
        "data_type":"cz",
        "data": []
    },

#司法部分—————————————————————————————
    #裁判文书
    "cpws": {
        "operation":"append",
        "data_type":"sf",
        "data": []
    }
}



#****************************************************************
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

#税务评级
taxRating = {
    "rowkey" : "",
    "rowkeySource" : "",
    "grade": "纳税等级",
    "year": "年份",
    "evalDepartment": "评价单位",
    "type": "0国税 1地税",
    "idNumber": "纳税人识别号",
    "name": "纳税人名称"
}

#网站备案
websiteRecode = {
    "rowkey" : "",
    "rowkeySource" : "",
    "examineDate" : "检查时间",
    "webName" : "网站名称",
    "webSite" : "网站首页",
    "ym" : "域名",
    "bah" : "备案号",
    "status" : "状态",
    "companyType" : "公司类型",
}

#债券信息
bondInfo = {
    "rowkey" : "",
    "rowkeySource" : "",
    "bondName": "债券名称",
    "bondNum": "债券代码",
    "publisherName": "发行人",
    "bondType": "债券类型",
    "publishExpireTime": "债劵到期日",
    "publishTime": "债劵发行日",
    "bondTimeLimit": "债劵期限",
    "ssjyr" : "上市交易日",
    "calInterestType": "计息方式",
    "bondStopTime": "债劵摘牌日",
    "xxpjjg" : "信用评级机构",
    "debtRating": "债项评级",
    "faceValue": "面值",
    "ccll" : "参考利率",
    "pmll" : "票面利率",
    "realIssuedQuantity": "实际发行量(亿)",
    "planIssuedQuantity": "计划发行量(亿)",
    "issuedPrice": "发行价格(元)",
    "lc" : "利差（BP）",
    "payInterestHZ": "付息频率",
    "startCalInterestTime": "债券起息日",
    "exeRightType": "行权类型",
    "xqrq" : "行权日期",
    "createTime": "发行日期",
    "escrowAgent": "托管机构",
    "flowRange": "流通范围",
}

#资质证书
qualificationCertificate = {
    "rowkey" : "",
    "rowkeySource" : "",
    "licenceType" : "证书类型",
    "zsbh" : "证书编号",
    "issueDate" : "发证日期",
    "jzrq" : "截止日期",
    "companyName" : "企业名称/申请人",
    "bz" : "标准",
    "ztbhsj" : "证书状态变化时间",
    "reason" : "原因",
    "scc" : "生产厂",
    "scfzrq" : "首次发证日期",
    "cpmc" : "产品名称",
    "zzs" : "制造商",
    "xinghao" : "型号/规格",
    "xzt" : "现状态",
    "ywzl" : "业务种类",
    "xkzbh" : "许可证编号",
    "ywfgfw" : "业务覆盖范围",
    "toDate" : "有效期至",
    "hm" : "号码",
    "sydw" : "使用单位",
    "pzyt" : "批准用途",
    "deviceName" : "设备名称",
    "deviceType" : "设备型号",
    "applyCompany" : "申请单位",
    "productCompany" : "生产企业",
}

#抽查检查
spotCheck = {
    "rowkey" : "",
    "rowkeySource" : "",
    "checkType" : "类型",
    "checkResult" : "结果",
    "checkOrg" : "检查实施机关",
    "checkDate" : "日期"
}

#产品信息
productInfo = {
    "rowkey" : "",
    "rowkeySource" : "",
    "classes" : "领域",
    "filterName" : "产品简称",
    "icon" : "图标",
    "type" : "产品分类",
    "brief" : "描述",
    "name" : "产品名称"
}

#招投标
bidding = {
    "rowkey" : "",
    "rowkeySource" : "",
    "content" : "整个内容源码",
    "title" : "标题",
    "purchaser" : "采购人",
    "abs" : "公告概要",
    "publishTime" : "发布时间",
    "proxy" : "公司名称",
    "link" : "原始链接",
    "intro" : "全部内容"  # 去掉源码中无用信息
}


impExpCredit = {
    "rowkey" : "",
    "rowkeySource" : "",
    "xydj":[
        {
        "creditRating" : "信用等级",
        "authenticationCode" : "认证证书编码",
        "identificationTime" : "认定时间"
        }
    ],
    "xzcf": [
        {
            "penaltyDate" : "处罚日期",
            "natureOfCase" : "案件性质",
            "decisionNumber" : "行政处罚决定书编号",
            "party" : "当事人"
        }
    ],
    "zcxx":
        {
            "industryCategory" : "行业种类",
            "validityDate" : "报关有效期",
            "annualReport" : "年报情况",
            "economicDivision" : "经济区划",
            "status" : "海关注销标识",
            "recordDate" : "注册日期",
            "managementCategory" : "经营类别",
            "administrativeDivision" : "行政区划",
            "crCode" : "海关注册号",
            "specialTradeArea" : "特殊贸易区域",
            "customsRegisteredAddress" : "注册海关",
            "types" : "跨境贸易电子商务类型"
        }
}

companyRelationship = {
    "rowkeySource": "rowkey来源",
    "rowkey":       "md5",
    "result": "json串"
}

#失信公告
sxgg = {
    "rowkeySource": "rowkey来源",
    "rowkey":       "md5",
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
    "rowkeySource":     "rowkey来源",
    "rowkey":           "md5",
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
    "rowkeySource":     "rowkey来源",
    "rowkey":           "md5",
    "sjly":             "数据来源",
    "sjlx":             "数据类别",
    "nsrmc":            "纳税人名称",
    "nsrsbh":           "纳税人识别码",
    "zzjgdm":           "组织机构代码",
    "dz":               "注册地址",
    "frxm":             "法定代表人或者负责人姓名",
    "frxb":             "法定代表人或者负责人性别",
    "frzjmc":           "法定代表人或者负责人证件名称",
    "cwfzrxm":          "负有直接责任的财务负责人姓名",
    "cwfzrxb":          "负有直接责任的财务负责人性别",
    "cwfzrzjmc":        "负有直接责任的财务负责人证件名称",
    "zjjg":             "负有直接责任的中介机构信息及其从业人员信息",
    "ajxz":             "案件性质",
    "wfss":             "主要违法事实",
    "yjcfqk":           "相关法律依据及税务处理处罚情况",
    "sbrq":             "案件上报期",
    "zxgxrq":           "最新更新日期"
    }

#政府采购严重违法失信信息
zfcgwf = {
    "rowkeySource":     "rowkey来源",
    "rowkey":           "md5",
    "sjly":             "数据来源",
    "sjlx":             "数据类别",
    "gysmc":            "供应商或代理机构名称",
    "dz":               "地址",
    "jtqx":             "不良行为的具体情形",
    "cfjg":             "处罚结果",
    "cfyj":             "处罚依据",
    "cfrq":             "处罚（记录）日期",
    "zfdw":             "执法（记录）单位",
    "cfjssj":           "处罚结束时间",
    "zxgxrq":           "最新更新日期"
    }
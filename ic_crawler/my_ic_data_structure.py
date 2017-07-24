#coding=utf-8
import json
result = {
    "errNum": 0,
    "abstract": "",
    "userID": "",
    "timeStamps": 1500004774,
    "errMsg":"success",
    "retData": {
        "TEL":"",           #(01)电话
        "EMAIL":"",         #(02)邮箱
        "SITE":"",          #(03)网址
        "ENTNAME ":"",      #(04)企业名称
        "REGNO":"",         #(05)工商注册号
        "ORGAN_CODE":"",    #(06)组织机构代码
        "NSRSBH":"",        #(07)纳税人识别号
        "UNISCID":"",       #(08)统一信用代码
        "LEREP":"",         #(09)法定代表人
        "ENTTYP":"",        #(10)类型
        "TRADE":"",         #(11)行业
        "REGCAP":"",        #(12)注册资本
        "ESTDATE":"",       #(13)成立日期
        "OPFROM":"",        #(14)经营期限自
        "OPTO":"",          #(15)经营期限至
        "REGORG":"",        #(16)登记机关
        "APPRDATE":"",      #(17)核准日期
        "DOM":"",           #(18)住所
        "REGSTAT":"",       #(19)登记状态
        "OPSCOPE":"",       #(20)经营范围
        "LEGINFO":[         #2股东信息
            {
                "ID": "",       #唯一标示
                "BLICNO": "",   #证照编号
                "BLICTYPE": "", #证照类型
                "INV    ": "",  #主管部门名称/股东/发起人名称
                "INVTYPE": "",  #主管部门类型/股东/发起人类型
                "INVDETAIL": {
                    "INV":"",   #主管部门名称/股东/发起人名称
                    "LISUBCONAM":"", #累计认缴额
                    "LIACCONAM":"",  #累计实缴额
                    "PUBDATE":"",    #公示日期
                    "CZRATIO":"",    #出资比例
                    "PAYINFO": [    
                        {
                        "CONFORM":"",   #认缴出资方式
                        "SUBCONAM":"",  #认缴出资额
                        "CONDATE":"",   #认缴出资日期
                        }
                    ],
                    "REALPAYINFO":[
                        {
                        "CONFORM":"",   #实缴出资方式
                        "ACCONAM":"",   #实缴出资额
                        "CONDATE":"",   #实缴出资日期
                        }
                    ],
                }
            }
        ],
        "PERINFO":[             #3主要人员信息
            {
                "NAME":"",      #姓名
                "POSITION":""   #职位
            }
        ],
        "BRANINFO":[            #4分支机构
            {
                "BRNAME ":"",   #名称
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
        ],
        "CHGINFO":[             #5变更信息
            {
                "ALTITEM ":"",  #变更事项
                "ALTDATE":"",   #变更日期
                "ALTBE":"",     #变更前内容
                "ALTAF":""      #变更后内容
            }
        ],
        "PUNINFO":[             #6行政处罚
            {
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
        ],
        "EXCEINFO":[     #7经营异常
            {
                "SPECAUSE":"",  #列入经营异常名录原因
                "ABNTIME":"",   #列入日期
                "REMEXCPRES":"",#移出经营异常名录
                "REMDATE":"",   #移出日期
                "DECORG":"",    #作出决定机关
                "YCCAUSE":"",   #移除原因
                "YCORG":""      #移除机关
            }
        ],
        "EQUINFO":[     #8股权出质
            {
                "EQUPLEDATE":"",    #股权出质登记日期
                "EQUITYNO":"",  #股权登记编号
                "TYPE":"", #状态
                "IMPAM":"", #出质股权数额
                "REGCAPCUR":"", #出质股权数额币种
                "PLEDAMUNIT":"",    #出质股权数额单位
                "PLEDGOR":"",   #出质人
                "PLEDNO":"",    #出质人证照号码（添加）
                "IMPORG":"",    #质权人
                "BLICNO ":"",   #质权人证照号码
                "BLICTYPE":"",  #质权人证照类型
                "REMARK":""     #备注
            }
        ],
        "MORTINFO":[     #9动产抵押
            {
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
        ],
        "QYGX":[],  #10企业关系
        "QYNB":[],  #11企业年报
        "DWTZ":[],  #12对外投资
        "FLSS":[],  #13法律诉讼
        "FYGG":[],  #14法院公告
        "SXR":[],  #15失信人
        "BZXR":[],  #16被执行人
        "LAWINFO":[ #17严重违法
            {
                "SERILLREA":"", #列入严重违法企业名单原因
                "ABNTIME":"",   #列入日期
                "REMDATE":"",   #移出日期
                "REMEXCPRES":"",#移出严重违法企业名单原因
                "DECORG":"作出决定机关",
                "":"",
                "":"",
            }
        ],
        "QSGG":[],  #18欠税公告
        "SBXX":[],  #19商标信息
        "ZL":[],  #20专利
        "ZZQ":[],  #21著作权
        "WZBA":[],  #22网站备案
        "RZLS":[],  #23融资历史
        "HXTD":[],  #24核心团队
        "QYYW":[],  #25企业业务
        "TZSJ":[],  #26投资事件
        "JPXX":[],  #27竞品信息
        "ZTB":[],  #28招投标
        "ZQXX":[],  #29债券信息
        "GDXX":[],  #30购地信息
        "ZPXX":[],  #31招聘信息
        "SWPJ":[],  #32税务评级
        "CCJC":[],  #33抽查检查
        "CPXX":[],  #34产品信息
        "ZZZS":[],  #35资质证书
        "FREEZEINFO": [ #36股权冻结信息
            {
                "BEEXECUTED":"",    #被执行人
                "EXECUTEDAM":"",    #股权数额
                "COURTDEPT":"",     #执行法院
                "REFERENCENUM":"",  #协助公示通知书文号
                "PUBDATE":"",       #公示日期
                "FREEZEFROM":"",    #冻结期限自
                "FREEZETO":"",      #冻结期限至
            }
        ]
    }
}


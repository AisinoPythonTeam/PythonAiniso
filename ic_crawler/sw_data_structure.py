#信用等级
{   "ENTNAME": "纳税人名称",
    "xydj": {
        "operation": "append",
        "data_type": "sw",
        "data":[]
    }
}
xydj = {
    "rowkeySource": "rowkey来源",
    "rowkey": "md5",
    "creditRating": "等级",
    "authenticationCode": "证书编号",
    "identificationTime": "认定时间",
    "nsrsbh": "纳税人识别号",
    "ssfj": "所属分局",
    "pjnd": "评价年度",
    "fbjg": "发布机构",
    "fbsj": "发布时间"
}


#欠税公告
{   "ENTNAME": "纳税人名称",
    "qsgg": {
        "operation": "append",
        "data_type": "sw",
        "data":[]
    }
}
qsgg = {
    "rowkeySource": "rowkey来源",
    "rowkey": "md5",
    "PUB_DATE": "发布日期", 
    "NSRSBH": "纳税人识别号",
    "TYPE": "欠税税种",
    "OW_REMAIN": "欠税币额",
    "OW_AMOUNT": "当前新发生的欠税余额",
    "TAX_AUTHORITY": "税务机关名称",
    "dom": "经营地点",
    "nsrlx": "纳税人类型",
    "LEREP": "负责人姓名 （法定代表人）",
    "id_type": "身份证件种类",
    "zj_no": "证件号码",
    "rdrq": "认定日期",
    "xqbz": "新欠币种",
    "qsssq": "欠税所属期",
    "sjly": "数据来源"
}

#行政许可
{   "ENTNAME": "纳税人名称",
    "xzxk": {
        "operation": "append",
        "data_type": "sw",
        "data":[]
    }
}
xzxk = {
    "rowkeySource": "rowkey来源",
    "rowkey": "md5",
    "xkjdwsh": "行政许可决定文书号",
    "splx": "审批类别/类型",
    "frdb": "法定代表人姓名、法人姓名",
    "nrxk": "许可内容",
    "xkyxq": "许可有效期",  
    "xkjzq": "许可截止期",
    "dfbm": "地方编码",
    "xkjg": "许可机关",
    
    "xmmc": "项目名称",
    "UNISCID": "统一社会信用代码",
    "ORGAN_CODE": "组织机构代码",
    "nsrsbh": "纳税人识别号",
    "REGNO": "工商登记码",
    "sedjh": "税务登记号",
    "wspzxh": "文书凭证序号",
    "zj_no": "法人证件号码",
    "xkjd_date": "许可决定日期",
    "xk_state": "许可状态、当前状态",
    "update_time": "数据更新时间",
    "beizhu": "备注",
    "shrq": "审核日期"
}

#税务登记及一般纳税人资格信息
{   "ENTNAME": "纳税人名称",
    "swdj_ybnsrzg": {
        "operation": "append",
        "data_type": "sw",
        "data":[]
    }
}
swdj_ybnsrzg = {
    "rowkeySource": "rowkey来源",
    "rowkey": "md5",
    "nsrsbh": "纳税人识别号",
    "nszg": "纳税资格名称",
    "LEREP": "法定代表人",
    "dom": "地址",
    "yxq_from": "有效期起",
    "zryxq_to": "暂认有效期止",
    "ssswjg": "所属税务机关",
    "yxq_to": "有效期止",
    "djzclx": "登记注册类型",
    "OPSCOPE": "经营范围",
    "pzsljg": "批准设立机关",
    "kjyw": "扣缴义务",
    "fzrq": "发证日期",
    "nsr_state": "纳税人状态",
    "nsrlb": "增值税纳税人类别"
}

#重大税收违法
{   "ENTNAME": "纳税人名称",
    "zdsswf": {
        "operation": "append",
        "data_type": "sw",
        "data":[]
    }
}
zdsswf = {
    "rowkeySource": "rowkey来源",
    "rowkey": "md5",
    "sjly": "数据来源",
    "sjlx": "数据类别",
    "nsrmc": "纳税人名称",
    "frxm": "法定代表人或者负责人姓名",
    "frxb": "法定代表人或者负责人性别",
    "frzjmc": "法定代表人或者负责人证件名称",
    "cwfzrxm": "负有直接责任的财务负责人姓名",
    "cwfzrxb": "负有直接责任的财务负责人性别",
    "cwfzrzjmc": "负有直接责任的财务负责人证件名称",
    "zjjg": "负有直接责任的中介机构信息及其从业人员信息",
    "ajxz": "案件性质",
    "wfss": "主要违法事实", #两个都赋值
    "yjcfqk": "相关法律依据及税务处理处罚情况", #两个都赋值
    "sbrq": "案件上报期",
    "zxgxrq": "最新更新日期",
    "nsrsbh": "纳税人识别码",
    "ORGAN_CODE": "组织机构代码",
    "dom": "注册地址",
    "LEREP": "法定代表人或者负责人姓名",
    "zrr": "自然人姓名",
    "zrr_sex": "自然人性别",
    "lerep_id_no": "法定代表人或者负责人证件号码",
    "lerep_info": "法定代表人或者负责人姓名、性别、证件名称及号码", 
    "zjcwfzr_id_no": "负有直接责任的财务负责人证件号码",
    "zjcwfzr_info": "负有直接责任的财务负责人姓名、性别、证件名称及号码",
    "sjfzr_info": "实际负责人姓名、性别及身份证号码（或其他证件号码）"
}
        
#失踪纳税人公告
{   "ENTNAME": "纳税人名称",
    "sznsrgg": {
        "operation": "append",
        "data_type": "sw",
        "data":[]
    }
}
sznsrgg = {
    "rowkeySource": "rowkey来源",
    "rowkey": "md5",
    "nsrsbh": "纳税人识别号",
    "LEREP": "法定代表人",
    "dom": "生产经营地址",
    "swjg": "税务机关名称",
    "zjlx": "证件类型",
    "zj_num": "法定代表人证件号码",
    "zclx": "登记注册类型：",
    "rjrq": "认定日期"
}

#行政处罚
{   "ENTNAME": "纳税人名称",
    "xzcf": {
        "operation": "append",
        "data_type": "sw",
        "data":[]
    }
}
xzcf = {
    "rowkeySource": "rowkey来源",
    "rowkey": "md5",
    "PENDECNO": "行政处罚决定文书号",
    "ILLEGACTTYPE": "违法行为类型", 
    "PENTYPE": "处罚种类", 
    "PENAM": "罚款金额", 
    "FORFAM": "没收金额", 
    "PENAUTH": "作出行政处罚决定单位名称",
    "PENDECISSDATE": "作出行政处罚决定日期",
    "LEREP": "法定代表人",
    "REMARK": "备注",
    "UNISCID": "统一社会信用代码",
    "nsrsbh": "纳税人识别号",
    "anmc": "案件名称",
    "person_name": "自然人或个体工商户名称",
    "zjlx": "证件类型",
    "zj_no": "法人证件号码",
    'cflb1': "处罚类别1",
    'cflb2': "处罚类别2",
    "cfsy": "处罚事由",
    "cfyj_jg": "处罚依据、处罚结果",
    "cfyj": "处罚依据",
    "cfjg": "处罚结果",
    "ORGAN_CODE": "组织机构代码",
    "REGNO": "工商登记码",
    "sedjh": "税务登记号",
    "xzxdr": "行政相对人名称",
    "wfdjrq": "违法行为登记日期",
    "cfjds_date": "处罚决定书制作日期",
    "cfsxq": "处罚生效期",
    "cfjzq": "处罚截止期",
    "dqzt": "当前状态",
    "dqclzt": "当前处理状态",
    'dfbm': "地方编码",
    'gsqx': "公示期限",
    'nsrzt': "纳税人状态",
    "gxsj": "更新时间"
}

#非正常户
{   "ENTNAME": "纳税人名称",
    "fzch": {
        "operation": "append",
        "data_type": "sw",
        "data":[]
    }
}
fzch = {
    "rowkeySource": "rowkey来源",
    "rowkey": "md5",
    "zggsjg": "主管国税机关",
    "nsrsbh": "纳税人识别号",
    "LEREP": "法定代表人",
    "zjlx": "证件类型",
    "id_no": "法定代表人身份证号码",
    "dom": "生产经营地址",
    "rdrq": "非正常认定日期",
    'fbrq':'发布日期',
    "zclx": "注册类型",
    "ORGAN_CODE": "组织机构代码",
    "qsbz": "欠税币种",
    "qssz": "欠税税种",
    "xqsje": "当前新发生的欠税金额",
    "kprq": "开票日期",
    "jkrq": "缴款期限",
    "qsje": "欠税金额",
    'sxrq':'证件失效确认日期',
    "beizhu": "备注"
}

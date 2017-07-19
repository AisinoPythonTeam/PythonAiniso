# -*- coding:utf-8 -*-
def get_base_post_paramaters(key, company_name=''):
    #列表信息
    search_formdata ={
        'mobileAction': 'entSearch',
        'keywords': u'%s' % '山西合盛达机电设备有限公司',
        'topic': '1',
        'pageNum': '1',
        'pageSize': '10',
        'userID': 'id001',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QuerySummary
    post:
        mobileAction	entSearch
        keywords	红麦聚信
        topic	1
        pageNum	1
        pageSize	10
        userID	id001
        userIP	192.123.123.13
    result:
        [{
            "BUSEXCEPTCOUNT": "0",
            "CAT18": "1",
            "CAT2NAME": "法定代表人",
            "ENTNAME": "<font color=red>红麦聚信</font>（北京）软件技术有限公司",
            "ENTTYPE": "1152",
            "ESTDATE": "2008年02月04日",
            "NAME": "马强",
            "PRIPID": "7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D1327479F643712858F53A206A04765BC89C69AAE4428305A637A0767EA30E8EC6EE5FF8930DA71D407BE1E05A3106893",
            "REGNO": "110108010799091",
            "REGSTATE_CN": "开业",
            "S_EXT_NODENUM": "110000",
            "UNISCID": "911101086723825825"
        }]
    """

    #基本信息：
    detail_formdata ={
        'mobileAction': 'entDetail',
        'userID': 'id001',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryBusiLice
    post:
        mobileAction	entDetail
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D5EB7603DAB556479322F640DEC4803571F2E3C634CD7C233A6894E5FA22683606EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        enttype	1152
        userID	id001
        userIP	192.123.123.13
    result:
        {
            "APPRDATE": "2016年12月12日",
            "CAT18": "1",
            "CAT2NAME": "法定代表人",
            "DOM": "北京市海淀区西北旺东路10号院东区7号楼二层E-216,E-219",
            "ENTNAME": "红麦聚信（北京）软件技术有限公司",
            "ENTTYPE_CN": "有限责任公司(法人独资)",
            "ESTDATE": "2008年02月04日",
            "NAME": "马强",
            "OPFROM": "2008年02月04日",
            "OPSCOPE": "技术开发、技术服务、技术咨询；基础软件服务、应用软件服务；销售自行开发后的产品；设计、制作、代理、发布广告。（企业依法自主选择经营项目，开展经营活动；依法须经批准的项目，经相关部门批准后依批准的内容开展经营活动；不得从事本市产业政策禁止和限制类项目的经营活动。）",
            "OPTO": "2028年02月03日",
            "REGCAP": "500.000000",
            "REGCAPCUR": "156",
            "REGCAPCUR_CN": "人民币元",
            "REGNO": "110108010799091",
            "REGORG_CN": "北京市工商行政管理局海淀分局",
            "REGSTATE_CN": "开业",
            "UNISCID": "911101086723825825"
        }
    """

    #股东及出资信息1
    czxx_formdata ={
        'mobileAction': 'invInfo',
        'userID': 'id001',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryInv
    post:
        mobileAction	invInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D3807BDAB7C14FD91871B48B1E78177DBE2939C6F7D7D233E1337C970CC68010E6EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        enttype	1152
        userID	id001
        userIP	192.123.123.13
    result:

    """
    #主要人员信息
    ryxx_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url:http://yd.gsxt.gov.cn/QueryPerson
    post:
        mobileAction	personInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D3807BDAB7C14FD91871B48B1E78177DBE2939C6F7D7D233E1337C970CC68010E6EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        pageNum	1
        pageSize	1
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #分支机构信息
    fzjg_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryBranch
    post:
        mobileAction	brchInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D3807BDAB7C14FD91871B48B1E78177DBE2939C6F7D7D233E1337C970CC68010E6EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #清算信息
    qsxx_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryAudit
    post:
        mobileAction	liqInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D3807BDAB7C14FD91871B48B1E78177DBE2939C6F7D7D233E1337C970CC68010E6EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #变更信息
    bgxx_formdata ={
        'mobileAction': 'altInfo',
        'startTime': '',
        'endTime': '',
        'userID': 'id001',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryChange
    post:
        mobileAction	altInfo
        startTime	
        endTime	
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D3807BDAB7C14FD91871B48B1E78177DBE2939C6F7D7D233E1337C970CC68010E6EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #动产抵押登记信息
    dcdy_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryMort
    post:
        mobileAction	moveInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D3807BDAB7C14FD91871B48B1E78177DBE2939C6F7D7D233E1337C970CC68010E6EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #股权出质登记信息
    gqcz_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryStoCz
    post:
        mobileAction	pledgeInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D3807BDAB7C14FD91871B48B1E78177DBE2939C6F7D7D233E1337C970CC68010E6EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        pageNum	1
        pageSize	10
        userID	id001
        userIP	192.123.123.13
    result:
    """
    #知识产权出质登记信息
    #商标注册信息
    sbzc_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryBrand
    post:
        mobileAction	tmInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D3807BDAB7C14FD91871B48B1E78177DBE2939C6F7D7D233E1337C970CC68010E6EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        pageNum	1
        pageSize	10
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #抽查检查结果信息
    jcjg_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryCheck
    post:
        mobileAction	spotInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D5EB7603DAB556479322F640DEC4803571F2E3C634CD7C233A6894E5FA22683606EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #司法协助信息
    sfxz_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryJudi
    post:
        mobileAction	judicialInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D5EB7603DAB556479322F640DEC4803571F2E3C634CD7C233A6894E5FA22683606EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #企业年报信息：
    qynb_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryAnnRepo
    post:
        mobileAction	ancheyearInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D5EB7603DAB556479322F640DEC4803571F2E3C634CD7C233A6894E5FA22683606EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        enttype	1152
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #股东及出资信息2
    gdjczxx2_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryEntInv
    post:
        mobileAction	instantInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D5EB7603DAB556479322F640DEC4803571F2E3C634CD7C233A6894E5FA22683606EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        enttype	1152
        pageNum	1
        pageSize	8
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #股权变更信息
    gqbg_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryEntSto
    post:
        mobileAction	changeInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D5EB7603DAB556479322F640DEC4803571F2E3C634CD7C233A6894E5FA22683606EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #行政许可信息
    xzxk_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryEntPerm
    post:
        mobileAction	licenseInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D5EB7603DAB556479322F640DEC4803571F2E3C634CD7C233A6894E5FA22683606EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #知识产权出质登记信息
    zscq_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryEntInteProp
    post:
        mobileAction	regInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D5EB7603DAB556479322F640DEC4803571F2E3C634CD7C233A6894E5FA22683606EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #行政处罚信息
    xzcf_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryEntPuni
    post:
        mobileAction	adpenaltyInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D5EB7603DAB556479322F640DEC4803571F2E3C634CD7C233A6894E5FA22683606EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #列入经营异常名录
    jyyc_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryAbnInfo
    post:
        mobileAction	abnormalInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D5EB7603DAB556479322F640DEC4803571F2E3C634CD7C233A6894E5FA22683606EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        enttype	1152
        userID	id001
        userIP	192.123.123.13
    result:
    """

    #严重违法失信企业名单（黑名单）
    yzwf_formdata ={
        'mobileAction': 'personInfo',
        'userID': 'id001',
        'pageNum': '1',
        'pageSize': '10',
        'userIP': '192.123.123.13'
    }
    """
    url: http://yd.gsxt.gov.cn/QueryBrLawInfo
    post:
        mobileAction	illegalInfo
        pripid	7804CD73F60B88AD3CA7442C3C70C640A8BCFE3D8C8D988CB5C1F1C7348D8A6D5EB7603DAB556479322F640DEC4803571F2E3C634CD7C233A6894E5FA22683606EE5FF8930DA71D407BE1E05A3106893
        nodenum	110000
        enttype	1152
        userID	id001
        userIP	192.123.123.13
    result:
    """
    return eval(key)
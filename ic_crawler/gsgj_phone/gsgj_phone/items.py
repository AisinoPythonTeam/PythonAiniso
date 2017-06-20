# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
class Item(scrapy.Item):
    #base
    UNISCID = scrapy.Field() #统一社会信用代码
    ENTNAME = scrapy.Field() #名称 || 企业名称
    ENTTYPE = scrapy.Field() #类型
    LEREP = scrapy.Field() #法定代表人 || 投资人
    REGCAP = scrapy.Field() #注册资本
    ESTDATE = scrapy.Field() #注册日期 || 成立日期
    OPFROM = scrapy.Field() #营业期限自
    OPTO = scrapy.Field() #营业期限至
    REGORG = scrapy.Field() #登记机关
    APPRDATE = scrapy.Field() #核准登记日期 || 核准日期
    REGSTATE = scrapy.Field() #登记状态
    DOM = scrapy.Field() #经营场所||住所
    OPSCOPE = scrapy.Field() #经营范围
    REGNO = scrapy.Field() #工商注册号 || 注册号
    ORGAN_CODE = scrapy.Field() #组织机构代码
    IXINNUOBM = scrapy.Field()
    ID = scrapy.Field()

    #1 czxx 股东及出资信息 
    LEGINFO = scrapy.Field()
    """ 
    BLICTYFLAGPE ：
    INVTYPE : 股东/发起人类型
    BLICNO ：证照编号
    INV ：股东/发起人名称
    ID ：唯一标示
    LISUBCONAM ：累计认缴额
    LIACCONAM ：累计实缴额
    PAYINFO ：一个列表包括
        CONDATE：认缴出资日
        CONFORM：认缴出资方
        SUBCONAM：认缴出资额
        REALPAYINFO ：一个列表包括
        ConDate：实缴出资日
        ConForm：实缴出资方
        AcConAm：实缴出资额
        
    """
    #2 ryxx主要人员信息 
    PERINFO = scrapy.Field()
    """
    NAME：姓名
    POSITION ：职务
    """

    #3 行政处罚
    PUNINFO = scrapy.Field()

    """
    PENDECNO : 处罚决定书文号
    ILLEGACTTYPE : 违法行为类型
    PENTYPE : 处罚种类
    PENAM : 罚款金额
    FORFAM : 没收金额
    PENAUTH : 作出行政处罚决定机关名称
    PENDECISSDATE : 作出处罚决定书日期
    """

    #4 bgxx 变更信息 
    CHGINFO = scrapy.Field()
    """
    ALTITEM : 变更事项
    ALTDATE : 变更日期
    ALTBE : 变更前内容
    ALTAF ：变更后内容
    """

    #5 经营异常信息
    EXCEINFO = scrapy.Field()    
    """
    SPECAUSE : 列入经营异常名录原因
    ABNTIME : 列入日期
    DECORG : 作出决定机关
    """

    #6 分支机构信息
    BRANINFO = scrapy.Field()
    """
    BRNAME : 名称
    LEREP : 法定代表人
    REGSTATE : 营业状态
    ESTDATE : 成立日期
    REGNO : 注册号
    DOM : 住所
    REGORG : 登记机关
    UNISCID : 统一社会信用代码
    TEL : 联系电话
    ADDR : 通信地址
    regCapital :
    category :

    """
    #7 股权出质登记信息
    EQUINFO = scrapy.Field()
    """
    EQUITYNO : 股权登记编号
    PLEDGOR : 出质人
    BLICTYPE : 质权人证照类型
    BLICNO : 质权人证照号码
    PLEDAMUNIT : 出质股权数额单位
    IMPAM : 出质股权数额
    REGCAPCUR : 出质股权数额币种
    IMPORG: 质权人
    EQUPLEDATE : 股权出质登记日期
    TYPE : 状态
    """
    #8 动产抵押登记信息
    MORTINFO = scrapy.Field()    
    """
    MORREGCNO : 动产抵押登记编号
    REGIDATE : 登记日期
    REGORG : 登记机关
    PRICLASECAM : 被担保债权数额
    TYPE : 状态
    PRICLASECKIND : 被担保债权种类
    REGCAPCUR : 被担保债权数额币种
    WARCOV : 担保范围
    PEFPERFORM : 债务人履行债务的期限自
    PEFPERTO : 债务人履行债务的期限至
    changeInfoList : 
    pawnInfoList : 
    peopleInfo : 
    """
    PARTNERCHAGEINFO = scrapy.Field()  #股东变更信息
    FREEZEINFO = scrapy.Field()  #司法股权冻结信息
    LAWINFO = scrapy.Field()     #严重违法信息
    industry = scrapy.Field()    #产业 天眼查
    company_md5 = scrapy.Field()
    company_id = scrapy.Field()
    crawl_time = scrapy.Field()  #采集时间
    detail_id = scrapy.Field()
    detail_formdata = scrapy.Field()
    czxx_formdata = scrapy.Field()
    ryxx_formdata = scrapy.Field()
    bgxx_formdata = scrapy.Field()
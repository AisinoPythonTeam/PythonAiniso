# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
class GjqyxyxxcxxtItem(scrapy.Item):
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
    #czxx
    LEGINFO = scrapy.Field()
    """
    name = scrapy.Field() #股东名称||合伙人
    name = scrapy.Field() #股东类型||合伙人类型
    name = scrapy.Field() #证照/证件类型 || 证照/证件号码 || 证照/证件编号
    name = scrapy.Field() #详情
    """
    #ryxx
    PERINFO = scrapy.Field()
    """
    name = scrapy.Field() #姓名
    name = scrapy.Field() #角色
    """
    #bgxx
    CHGINFO = scrapy.Field()
    """
    name = scrapy.Field() #变更事项
    name = scrapy.Field() #变更前内容
    name = scrapy.Field() #变更后内容
    name = scrapy.Field() #变更日期
    """
    #ryjgxx
    BRANINFO = scrapy.Field() #分支机构信息
    PARTNERCHAGEINFO = scrapy.Field()  #股东变更信息
    MORTINFO = scrapy.Field()    #动产抵押登记信息
    EQUINFO = scrapy.Field()     #股权出质登记信息
    FREEZEINFO = scrapy.Field()  #司法股权冻结信息
    LAWINFO = scrapy.Field()     #严重违法信息
    EXCEINFO = scrapy.Field()    #经营异常信息
    PUNINFO = scrapy.Field()     #行政处罚

    industry = scrapy.Field()    #产业 天眼查
    company_md5 = scrapy.Field()
    company_id = scrapy.Field()
    crawl_time = scrapy.Field()  #采集时间
    detail_id = scrapy.Field()
    detail_formdata = scrapy.Field()
    czxx_formdata = scrapy.Field()
    ryxx_formdata = scrapy.Field()
    bgxx_formdata = scrapy.Field()
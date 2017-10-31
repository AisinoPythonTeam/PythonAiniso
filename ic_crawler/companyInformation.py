#coding=utf-8
#企业信息
companyInformation = {
    #——————gs—————————————————————————————————————————
    #1  BASIC           基本信息        
    #2  LEGINFO         股东信息        
    #3  PERINFO         主要人员信息    
    #4  BRANINFO        分支机构        
    #5  CHGINFO         变更信息        
    #6  EXCEINFO        经营异常        
    #7  EQUINFO         股权出质        
    #8  MORTINFO        动产抵押        
    #9  INVEST          对外投资        
    #10 LAWINFO         严重违法        
    #11 TMINFO          商标信息        
    #12 PATENT          专利            
    #13 COPYRIGHT       著作权          
    #14 FREEZEINFO      股权冻结信息    
    #15 WEBSITERECODE   网站备案        
    #16 BONDINFO        债券信息        
    #17 QFCF            资质证书        
    #18 PRODUCTINFO     产品信息        
    #19 RELATIONSHIP    企业关系        
    #20 SENIORPEOPLE    高管信息        
    #21 ABNORMALDIR     异常名录        
    #22 ADMINISTLIC     行政许可        
    #23 PUNINFO         行政处罚、重点关注名单  
    
    #——————sf—————————————————————————————————————————
    #24 SPOTCHECK       抽查检查        
    #25 BPNOTICE        失信公告、失信被执行人 
    #26 REFEREEDOC      裁判文书       
    #27 IOCREDIT        进出口信用     
    
    #——————sw—————————————————————————————————————————
    #28 CREDITLEVEL     信用等级  守信红名单、税务评级  
    #29 OTNOTICE        欠税公告                        
    #30 TAXREGIST       税务登记及一般纳税人资格信息    
    #31 TAXCONTRAVE     重大税收违法                    
    #32 MISSNOTICE      失踪纳税人公告                  
    #33 IMPROPER        非正常户                        
    
    #——————cz—————————————————————————————————————————
    #34 PURCHASEBL      政府采购严重违法失信信息        
    #35 BID             招投标                           
}

#——————gs——————
BASIC         = {"operation":"replace", "data_type":"gs_V1", "data": []}
LEGINFO       = {"operation":"replace", "data_type":"gs_V1", "data": []}
PERINFO       = {"operation":"replace", "data_type":"gs_V1", "data": []}
BRANINFO      = {"operation":"append",  "data_type":"gs_V1", "data": []}
CHGINFO       = {"operation":"append",  "data_type":"gs_V1", "data": []}
EXCEINFO      = {"operation":"append",  "data_type":"gs_V1", "data": []}
EQUINFO       = {"operation":"append",  "data_type":"gs_V1", "data": []}
MORTINFO      = {"operation":"append",  "data_type":"gs_V1", "data": []}
INVEST        = {"operation":"append",  "data_type":"gs_V1", "data": []}
LAWINFO       = {"operation":"append",  "data_type":"gs_V1", "data": []}
TMINFO        = {"operation":"append",  "data_type":"gs_V1", "data": []}
PATENT        = {"operation":"append",  "data_type":"gs_V1", "data": []}
COPYRIGHT     = {"operation":"append",  "data_type":"gs_V1", "data": []}
FREEZEINFO    = {"operation":"append",  "data_type":"gs_V1", "data": []}
WEBSITERECODE = {"operation":"append",  "data_type":"gs", "data": []}
BONDINFO      = {"operation":"append",  "data_type":"gs", "data": []}
QFCF          = {"operation":"append",  "data_type":"gs", "data": []}
PRODUCTINFO   = {"operation":"append",  "data_type":"gs", "data": []}
RELATIONSHIP  = {"operation":"replace", "data_type":"gs", "data": []}
SENIORPEOPLE  = {"operation":"replace", "data_type":"gs", "data": []}
ABNORMALDIR   = {"operation":"append",  "data_type":"gs", "data": []}
ADMINISTLIC   = {"operation":"append",  "data_type":"gs", "data": []}
PUNINFO       = {"operation":"append",  "data_type":"gs", "data": []}
#——————sf——————
SPOTCHECK     = {"operation":"append",  "data_type":"sf", "data": []}
BPNOTICE      = {"operation":"append",  "data_type":"sf", "data": []}
REFEREEDOC    = {"operation":"append",  "data_type":"sf", "data": []}
IOCREDIT      = {"operation":"append",  "data_type":"sf", "data": []}
#——————sw——————                         
CREDITLEVEL   = {"operation":"append",  "data_type":"sw", "data": []}
OTNOTICE      = {"operation":"append",  "data_type":"sw", "data": []}
TAXREGIST     = {"operation":"append",  "data_type":"sw", "data": []}
TAXCONTRAVE   = {"operation":"append",  "data_type":"sw", "data": []}
MISSNOTICE    = {"operation":"append",  "data_type":"sw", "data": []}
IMPROPER      = {"operation":"append",  "data_type":"sw", "data": []}
#——————cz——————                         
PURCHASEBL    = {"operation":"append",  "data_type":"cz", "data": []}
BID           = {"operation":"append",  "data_type":"cz", "data": []}
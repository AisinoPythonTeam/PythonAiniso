#coding=utf-8
#企业信息
companyInformation = {
    #——————————————————————————————————————————————————————————————————————————
    #1  LEGINFO                     股东信息        
    #2  PERINFO                     主要人员信息    
    #3  BRANINFO                    分支机构        
    #4  CHGINFO                     变更信息        
    #5  EXCEINFO                    经营异常        
    #6  EQUINFO                     股权出质        
    #7  MORTINFO                    动产抵押        
    #8  TMINFO                      商标信息        
    #9  PATENT                      专利            
    #10 COPYRIGHT                   著作权          
    #11 FREEZEINFO                  股权冻结信息    
    #12 INVEST                      对外投资        
    #13 TOWNTAX                     欠税公告
    #14 PUNINFO                     行政处罚
    #15 LAWINFO                     严重违法        
    
    #16 productInfo                 产品信息        
    #17 bondInfo                    债券信息      
    #18 companyRelationship         企业关系        
    #19 seniorPeople                高管信息        
    #20 websiteRecode               网站备案        
    #21 basicInfo                   基本信息        
    #22 spotCheck                   抽查检查        
    #23 impExpCredit                进出口信用 
    #24 qualificationCertificate    资质证书        
    #25 taxRating                   税务评级|信用等级|守信红名单        
    #26 bidding                     招投标       
    #27 taxContrave                 重大税收违法                    
    #28 taxRegist                   税务登记及一般纳税人资格信息    
    #29 missNotice                  失踪纳税人公告                  
    #30 impRoper                    非正常户   
    #31 dishonestyNotice            失信公告                        
    #32 administrativeLicensing     行政许可
    #33 purchaseIllegal             政府采购严重违法失信信息

    #34 administrativePenalty       行政处罚2（xyzg+sw）
    #35 owingTaxesNotice            欠税公告2  sw 
}

LEGINFO                 ={"operation":"replace", "data_type":"gs_V1", "data": []}
PERINFO                 ={"operation":"replace", "data_type":"gs_V1", "data": []}
BRANINFO                ={"operation":"append",  "data_type":"gs_V1", "data": []}
CHGINFO                 ={"operation":"append",  "data_type":"gs_V1", "data": []}
EXCEINFO                ={"operation":"append",  "data_type":"gs_V1", "data": []}
EQUINFO                 ={"operation":"append",  "data_type":"gs_V1", "data": []}
MORTINFO                ={"operation":"append",  "data_type":"gs_V1", "data": []}
INVEST                  ={"operation":"append",  "data_type":"gs_V1", "data": []}
LAWINFO                 ={"operation":"append",  "data_type":"gs_V1", "data": []}
TMINFO                  ={"operation":"append",  "data_type":"gs_V1", "data": []}
PATENT                  ={"operation":"append",  "data_type":"gs_V1", "data": []}
COPYRIGHT               ={"operation":"append",  "data_type":"gs_V1", "data": []}
FREEZEINFO              ={"operation":"append",  "data_type":"gs_V1", "data": []}
PUNINFO                 ={"operation":"append",  "data_type":"gs_V1", "data": []}
TOWNTAX                 ={"operation":"append",  "data_type":"sw",    "data": []}
basicInfo               ={"operation":"replace", "data_type":"gs_V1", "data": []}

productInfo             ={"operation":"append",  "data_type":"gs",    "data": []}
bondInfo                ={"operation":"append",  "data_type":"gs",    "data": []}
companyRelationship     ={"operation":"replace", "data_type":"gs",    "data": []}
seniorPeople            ={"operation":"replace", "data_type":"gs",    "data": []}
websiteRecode           ={"operation":"append",  "data_type":"gs",    "data": []}
spotCheck               ={"operation":"append",  "data_type":"gs",    "data": []}
impExpCredit            ={"operation":"append",  "data_type":"gs",    "data": []}
administrativeLicensing = {"operation":"append", "data_type":"gs",    "data": []}
administrativePenalty   ={"operation":"append",  "data_type":"gs",    "data": []}

taxRating               ={"operation":"append",  "data_type":"sw",    "data": []}
taxContrave             ={"operation":"append",  "data_type":"sw",    "data": []}
missNotice              ={"operation":"append",  "data_type":"sw",    "data": []}
taxRegist               ={"operation":"append",  "data_type":"sw",    "data": []}
impRoper                ={"operation":"append",  "data_type":"sw",    "data": []}
owingTaxesNotice        ={"operation":"append",  "data_type":"sw",    "data": []}

bidding                 ={"operation":"append",  "data_type":"cz",    "data": []}
purchaseIllegal         ={"operation":"append",  "data_type":"cz",    "data": []}

dishonestyNotice        ={"operation":"append",  "data_type":"sf",    "data": []}



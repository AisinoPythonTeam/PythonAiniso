# -*- coding: utf-8 -*-

BOT_NAME = 'gsgj_phone'

SPIDER_MODULES = ['gsgj_phone.spiders']
NEWSPIDER_MODULE = 'gsgj_phone.spiders'

COOKIES_ENABLES = False

DEFAULT_HEADERS = {
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 Html5Plus/1.0',
                'Accept-Language': 'zh-cn',
                'Connection':'keep-alive',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Referer': 'http://yd.gsxt.gov.cn/QuerySummary'
}

COMPANIES = 'companies'
RETRY_ENABLED = False

#mongo________________________________________________________
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_AUTH_USER = 'liurj'
MONGO_AUTH_PWD = 'liurj'

#queue________________________________________________________
QUEUE_REDIS_HOST = '127.0.0.1'
QUEUE_REDIS_PORT = 6379

#uniq_________________________________________________________
UNIQ_REDIS_HOST = '127.0.0.1'
UNIQ_REDIS_PORT = 6379

#log__________________________________________________________
LOG_FILE = '/Users/liurongjiang/git_test/PythonAiniso/ic_crawler/gsgj_phone/logs/crawler.log'
LOG_LEVEL = 'DEBUG'

DOWNLOADER_MIDDLEWARES = {
    'gsgj_phone.my_middlewares.ProxyMiddleware': 100,
    'gsgj_phone.my_middlewares.MyUserAgentMiddleware': 200
}

ITEM_PIPELINES = {
    'gsgj_phone.pipelines.MyPipeline': 100
}

DOWNLOAD_TIMEOUT = 30
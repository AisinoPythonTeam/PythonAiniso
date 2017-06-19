# -*- coding: utf-8 -*-

# Scrapy settings for gjqyxyxxcxxt project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'gjqyxyxxcxxt'

SPIDER_MODULES = ['gjqyxyxxcxxt.spiders']
NEWSPIDER_MODULE = 'gjqyxyxxcxxt.spiders'
COOKIES_ENABLES = False

DEFAULT_HEADERS = {
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 Html5Plus/1.0',
                'Accept-Language': 'zh-cn',
                'Connection':'keep-alive',
                'Accept-Encoding': 'gzip, deflate',
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
LOG_FILE = '../crawler.log'
LOG_LEVEL = 'DEBUG'

DOWNLOADER_MIDDLEWARES = {
    #'gjqyxyxxcxxt.user_agent_middleware.ProxyMiddleware': 100,
    'gjqyxyxxcxxt.user_agent_middleware.MyUserAgentMiddleware': 200,
}

ITEM_PIPELINES = {
    'gjqyxyxxcxxt.pipelines.GjqyxyxxcxxtPipeline': 100
}
DOWNLOAD_TIMEOUT = 10

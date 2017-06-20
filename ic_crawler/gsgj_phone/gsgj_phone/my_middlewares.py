# -*- coding:utf-8 -*-
import requests
import os, base64, urllib, random
from scrapy import log
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
class ProxyMiddleware(object):
    #下载页面前调用,更改请求url地址
    def process_request(self, request, spider):
        #启用代理
        proxy = requests.get('http://api.ip.data5u.com/dynamic/get.html?order=68fcb9ab2ed1d14577ecb31b9c3c786f&sep=3')
        request.meta['proxy'] = "http://%s" % proxy.text.strip()
        """
        if 'is_proxy' in request.meta and request.meta['is_proxy']:
            request.meta['proxy'] = "http://204.74.210.83:53760"
            # Use the following lines if your proxy requires authentication
            proxy_user_pass = "kunzhipeng:kHxG6QDp"
            # setup basic authentication for the proxy
            encoded_user_pass = base64.encodestring(proxy_user_pass)
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
        """
        log.msg('proxy:%s' % request.meta['proxy'],level=log.DEBUG)

    #下载页面后调用,恢复原始url地址
    def process_response(self, request, response, spider):
        return response

class MyUserAgentMiddleware(UserAgentMiddleware):
    """ 覆盖原始use_agent
        """
    user_agent_list = [
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F136 Safari/525.20",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A334 Safari/7534.48.3",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A405 Safari/7534.48.3",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25",
        "Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; IS01 Build/S3082) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; IS01 Build/SA180) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; Docomo HT-03A Build/DRD08) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; SonyEricssonSO-01B Build/R1EA029) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; generic Build/Donut) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03S) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
    ]

    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        agent_list = self.user_agent_list
        agent = random.choice(agent_list)
        if agent:
            request.headers.setdefault('User-Agent', agent)

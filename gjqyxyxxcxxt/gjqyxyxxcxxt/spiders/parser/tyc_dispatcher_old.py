# -*- coding:utf-8 -*-
import re, json, time, codecs, urllib, requests, click
from tyc_conf_and_parse import get_conf,        \
                               get_url,         \
                               base_info_parse, \
                               get_token_and_utm,\
                               czxx_parse,      \
                               ryxx_parse,      \
                               xzcf_parse,      \
                               bgxx_parse,      \
                               ycxx_parse,      \
                               fzjg_parse

class TianYanCha():
    item = None
    session = requests.session()
    session.cookies.set("tnet", "123.114.125.92")
    referer_url = get_conf('referer_url')
    public_headers = get_conf('public_headers')
    api_headers = public_headers.copy()
    api_headers.update(get_conf('my_headers'))
    tj_url = 'http://www.tianyancha.com/tongji/%s.json?random=%s'

    def get_create_cookies(self, c_name):
        tongji_url = self.tj_url % (c_name, (int(time.time()) * 1000))
        self.get_token_utm(tongji_url)

    def get_token_utm(self, tongji_url):
        tongji_page = self.session.request("GET", tongji_url, headers=self.api_headers)
        token, utm = get_token_and_utm(tongji_page)
        self.session.cookies.set("token", token)
        self.session.cookies.set("_utm", utm)

    def __get_list_info(self, company_name):
        data_page = self.session.request("GET", get_url('list_url', company_name), headers=self.api_headers)
        source = data_page.content.decode('utf-8')
        json_obj = json.loads(source)
        return json_obj['data']

    def __get_all_info(self, item, info_key, url_param):
        url = get_url(info_key + '_url', url_param)
        response = self.session.request("GET", url, headers=self.api_headers)
        content = response.content.decode('utf-8')
        try:
            json_object = json.loads(content)
        except:
            return []
        if json_object['data'] == 'null' or json_object['data'] == None:
            return []
        defined_key, result = eval(info_key+'_parse')(json_object)
        item[defined_key] = result
        print 'info_key: ', info_key
        print 'defined_key: ', defined_key
        print '--->:   ', result


    def _dispatcher(self, company_name):
        if isinstance(company_name, unicode):
            company_name = urllib.quote(company_name.encode('utf-8'))
        self.get_create_cookies(company_name)
        
        items = []
        results = self.__get_list_info(company_name)

        print len(results)
        item = None
        for result in results:
            res = base_info_parse(result)
            if item is None:
                item = res
            elif len(res['ENTNAME']) < len(item['ENTNAME']):
                item = res

        if item is not None:
            self.__get_all_info(item, 'czxx', item['company_id'])   #1
            self.__get_all_info(item, 'ryxx', item['company_id'])   #2
            self.__get_all_info(item, 'xzcf', item['ENTNAME'])   #item['ENTNAME']
            self.__get_all_info(item, 'bgxx', item['company_id'])
            self.__get_all_info(item, 'ycxx', item['company_id'])
            self.__get_all_info(item, 'fzjg', item['company_id'])
            items.append(item)
        return items

def run(company_name):
    tyc = TianYanCha()
    res = tyc._dispatcher(company_name)
    if res:
        return res[0]
    return None

@click.command()
@click.option('--company_name', default=None, help='entry company to crawl')
def test(company_name):
    if not company_name:
        print 'company_name is None!!!'
        return None
    tyc = TianYanCha()
    res = tyc._dispatcher(company_name)
    print res
    print len(res)

if __name__ == '__main__':
    test()
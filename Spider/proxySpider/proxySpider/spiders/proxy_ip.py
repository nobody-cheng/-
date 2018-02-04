# -*- coding: utf-8 -*-
import scrapy
from proxySpider.items import ProxyspiderItem
import requests
import re

class ProxyIpSpider(scrapy.Spider):
    name = 'proxy_ip'
    allowed_domains = ['proxy.coderbusy.com']
    start_urls = ['https://proxy.coderbusy.com/']

    # def start_requests(self):
    #     start_urls = ['https://proxy.coderbusy.com/']
    #     session = requests.Session()
    #     response = session.get(start_urls[0], timeout=5)
    #     dict_cookie = requests.utils.dict_from_cookiejar(response.cookies)
    #     yield scrapy.Request(
    #         'http://www.kuaidaili.com/free/',
    #         callback=self.parse,
    #         cookies=dict_cookie
    #     )

    def parse(self, response):
        """得到ip和端口号,类型,服务器地址"""

        print('解析ip,port,type')
        tr_list = response.xpath(".//table[@class='table proxy-server-table']/tbody/tr")

        for tr in tr_list:
            print('===========================', tr)
            item = ProxyspiderItem()
            item['ip'] = tr.xpath("./td/text()").extract_first() if len(tr.xpath("./td[1]/text()")) else None
            # item['port'] = tr.xpath("./td[2]/text()").extract_first() if len(tr.xpath("./td[3]/text()")) else None
            # item['style'] = tr.xpath("./td[4]/text()").extract_first() if len(tr.xpath("./td[6]/text()")) else None
            # item['addr'] = tr.xpath("./td[5]/text()").extract_first() if len(tr.xpath("./td[4]/text()")) else None
            # item['hide'] = tr.xpath("./td[3]/text()").extract_first() if len(tr.xpath("./td[5]/text()")) else None
            print('+++++++++++++++++++++++++++++++', item['ip'])

            # # 下一页
            # i = 1
            # while i <=1981:
            #     next_url= 'http://www.kuaidaili.com/free/'+"free/inha/{}/".format(i)
            #     i += 1

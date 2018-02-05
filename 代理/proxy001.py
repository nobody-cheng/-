# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import requests
import json

proxy_list = []
i = 0


class Proxy001Spider(CrawlSpider):
    name = 'proxy001'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://www.kuaidaili.com/free/inha/{}/']




    def start_requests(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
                        "Referer":"http://www.kuaidaili.com/free/inha/1/"}
        cookies = "yd_cookie=8a30451e-d084-4d23a79198f99a90b14271bab6dd6ee333fe; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1513602692; _ga=GA1.2.227259048.1513602692; _gid=GA1.2.146967798.1513602692; channelid=0; sid=1513665018301216; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1513665890; _ydclearance=6d85dd7c0189fdda0042c69e-6862-42e9-84a4-303d0f238f13-1513680769"
        self.cookies_dict ={i.split("=")[0]:i.split("=")[-1] for i in cookies.split("; ")}
        # print(cookies_dict)

        yield scrapy.Request(
            self.start_urls[0].format(1),
            cookies=self.cookies_dict,
            headers = self.headers,
            callback= self.parse_item

        )


    def parse_item(self, response):
        content_list = response.xpath(".//table[@class='table table-bordered table-striped']//tbody/tr")
        print("="*100)
        # 总页数
        total = response.xpath(".//div[@id='listnav']/ul//text()").extract()[-2]
        total = int(total)
        # print(type(total))

        for i in content_list:
            item = {}
            item["ip"] = i.xpath(".//td[1]/text()").extract_first()
            item["prot"] = i.xpath(".//td[2]/text()").extract_first()
            item["匿名度"] = i.xpath(".//td[3]/text()").extract_first()
            item["类型"] = i.xpath(".//td[4]/text()").extract_first()
            # item["位置"] = i.xpath(".//td[5]/text()").extract_first()
            # item["响应速度"] = i.xpath(".//td[6]/text()").extract_first()
            # item["最后验证时间"] = i.xpath(".//td[7]/text()").extract_first()
            item_json = json.dumps(item, ensure_ascii=False, indent=2)
            print(item)
            with open("proxy.txt", "a") as f:
                f.write(item_json)
            proxy_list.append(item)
            if i < total+1:
                global i
                i +=1
                self.headers["Referer"] = "http://www.kuaidaili.com/free/inha/{}/".format(i-1)
                yield scrapy.Request(
                    self.start_urls[0].format(i),
                    cookies=self.cookies_dict,
                    headers=self.headers,
                    callback=self.parse_item
                )
                # return item

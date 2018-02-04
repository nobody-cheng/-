# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

i = 1


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0']

    rules = (

        Rule(
            LinkExtractor(allow=r'id=\d+&keywords=&tid=0&lid=0'),  # 爬取详情页
            callback='parse_details',
            follow=False,
        ),

        Rule(
            LinkExtractor(allow=r'start=\d+'),  # 爬取url规则
            callback='parse_item',  # 回调函数
            follow=True  # url地址继续被提取
        ),

    )

    def parse_item(self, response):
        items = response.xpath("//tr[contains(@class,'odd') or contains(@class,'even')]")
        for item in items:
            global i
            temp = {}
            temp['job'] = item.xpath(".//td[1]/a/text()").extract_first()
            temp['detailLink'] = "http://hr.tencent.com/" + item.xpath(".//td[1]/a/@href").extract_first()
            temp['Category'] = item.xpath(".//td[2]/text()").extract_first() if len(
                item.xpath(".//td[2]/text()")) > 0 else '无分类'
            temp['num'] = item.xpath(".//td[3]/text()").extract_first()
            temp['addr'] = item.xpath(".//td[4]/text()").extract_first()
            temp['date_time'] = item.xpath(".//td[5]/text()").extract_first()
            # print('````````````第{}条招聘```````````````'.format(i), temp)
            # print(item)
            i += 1
            print(item)
            yield item

    def parse_details(self, response):
        item = {}
        item['duty'] = response.xpath("//table[@class='tablelist textl']/tr[3]/td/ul//li/text()").extract()
        item['req'] = response.xpath("//table[@class='tablelist textl']/tr[4]/td/ul//li/text()").extract()
        # print(item['duty'])
        # print(item['req'])
        yield item

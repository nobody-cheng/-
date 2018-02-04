# -*- coding: utf-8 -*-
import scrapy
from sina.items import SinaItem


class SinaNewSpider(scrapy.Spider):
    print('`````````````````````````````````````````')
    name = 'sina_new'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    # redis_key = "sina"

    def parse(self, response):
        # 得到所有大分类
        div_list = response.xpath("//div[@id='tab01']//div")

        for div in div_list:
            item = SinaItem()
            item['b_title'] = div.xpath("./h3/a/text()").extract_first()
            li_list = div.xpath("./ul//li")
            for li in li_list:
                item['s_title'] = li.xpath("./a/text()").extract_first()
                item['s_url'] = li.xpath("./a/@href").extract_first()
                yield scrapy.Request(
                    item['s_url'],
                    meta={'item': item},
                    callback=self.second_parse
                )

    def second_parse(self, response):
        """每类新闻列表,得到每条新闻的链接"""
        item = response.meta['item']
        # 每条新闻的列表
        a_url_list = response.xpath("//a/@href").extract()
        for a_url in a_url_list:
            item['a_url'] = a_url
            if a_url.endswith('.shtml'):
                yield scrapy.Request(
                    item['a_url'],
                    meta={'item': item},
                    callback=self.detail_parse
                )

    def detail_parse(self, response):
        """每条新闻的详细链接,得到标题,正文,时间"""
        item = response.meta['item']

        item['head'] = response.xpath("//h1[@class='main-title']/text()").extract_first()


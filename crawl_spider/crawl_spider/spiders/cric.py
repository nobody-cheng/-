# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CricSpider(CrawlSpider):
    name = 'cric'
    allowed_domains = ['circ.gov.cn']
    start_urls = ['http://www.circ.gov.cn/web/site0/tab5240/']

    rules = (
        #LinkExtractor 连接提取器，提取url地址,正则不用完全匹配，匹配到一部分，就会请求这个url地址
        #callback 提取出来的url交给哪个函数去处理，字符串
        #follow 提取出来的url地址的响应会继续呗Rule来提取url地址
        #提取详情页的url地址
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+.htm$'),callback="parse_detail"),
        #提取翻页的url地址
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/module14430/page\d+.htm$'),follow=True),
    )

    def parse_detail(self, response):
        item = {}
        item["article_title"] =  response.xpath("//*[@id='tab_content']/tbody/tr[1]/td/text()").extract()

        print(item)

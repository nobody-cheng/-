# -*- coding: utf-8 -*-
import scrapy
from jd.items import JdItem

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath("//div[@class='mc']/dl//dt")
        for dt in dt_list:
            print('dl_list', dt_list)
            print('dl', dt)
            item = JdItem()
            item['b_class'] = dt.xpath("./a/text()").extract_first()
            print(item)
            break

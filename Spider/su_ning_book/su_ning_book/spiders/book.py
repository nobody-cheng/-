# -*- coding: utf-8 -*-
import scrapy
from su_ning_book.items import SuNingBookItem
from copy import deepcopy
import re
import json


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['suning.com']
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']

    def parse(self, response):
        """处理数据的提取和url的提取"""
        # resposne是start_url地址的响应
        print('*' * 100)
        li_list = response.xpath("//ul[@class='ulwrap']//li")  # 获取到图书的大分类
        for li in li_list:
            item = SuNingBookItem()
            item['b_class'] = li.xpath("./div[1]/a/text()").extract_first()
            a_list = li.xpath("./div[2]/a")  # 获取到图书的小分类
            for a in a_list:
                item['s_class'] = a.xpath("./text()").extract_first()  # 小分类的名字
                item['s_href'] = a.xpath("./@href").extract_first()  # 小分类的地址
                item['s_href'] = 'http://snbook.suning.com' + item['s_href']  # 拼接地址
                if item['s_href'] is not None:
                    # 请求小分类的地址
                    yield scrapy.Request(
                        item['s_href'],
                        self.parse_book_list,  # 列表页
                        meta={'item': deepcopy(item)},
                    )

    def parse_book_list(self, response):

        """列表页面"""
        item = response.meta['item']
        li_list = response.xpath(".//div[@class='filtrate-books list-filtrate-books']/ul//li")  # 取得列表页所有的图书

        for li in li_list:
            # 页面的详情信息,图片,书名,作者,出版社,简介,详情页面连接
            item['book_img'] = li.xpath(".//div[@class='book-img']//img/@src").extract_first() if len(li.xpath(".//div[@class='book-img']//img/@src"))>0 else '未找到封面'
            if item['book_img'] is None:
                item['book_img'] = li.xpath(".//div[@class='book-img']//img/@src").extract_first() if len(
                    li.xpath(".//div[@class='book-img']//img/@src2")) > 0 else '未找到封面'

            item['title'] = li.xpath(".//div[@class='book-title']/a/@title").extract_first() if len(li.xpath(".//div[@class='book-title']/a/@title"))>0 else '未找到图书'
            item['book_author'] = li.xpath(".//div[@class='book-author']/a/text()").extract_first() if len(li.xpath(".//div[@class='book-author']/a/text()"))>0 else '未找到作者'
            item['book_press'] = li.xpath(".//div[@class='book-publish']/a/text()").extract_first() if len(li.xpath(".//div[@class='book-publish']/a/text()"))>0 else '未找到出版社'
            item['book_desc'] = li.xpath(".//div[@class='book-descrip c6']/text()").extract_first() if len(li.xpath(".//div[@class='book-descrip c6']/text()"))>0 else '无详情页'
            item['book_href'] = li.xpath(".//div[@class='book-title']/a/@href").extract_first() if len(li.xpath(".//div[@class='book-title']/a/@href"))>0 else '无链接'
            # 请求详情页面信息
            if item['book_href'] is not None:
                yield scrapy.Request(
                    item['book_href'],
                    self.parse_book,
                    meta={'item': deepcopy(item)}
                )
        # 列表也翻页---在response中找到与页码有关的数据 var pagecount=2;var currentPage=1,共有2页,第一页
        page_count = re.findall("var pagecount=(.*?);", response.body.decode())[0]
        page_current = re.findall("var currentPage=(.*?);", response.body.decode())[0]

        if int(page_current) < int(page_count):
            next_url = item['s_href'] + "?pageNumber={}&sort=0".format(int(page_current) + 1)
            yield scrapy.Request(
                next_url,
                method='POST',
                body=json.dumps({"ajaxFlag": "true"}),  # 这里需要传入的是一个字符串
                callback=self.parse_book_list,
                meta={"item": item}  # 必须传，去meta中的item会报错
            )

    def parse_book(self, response):
        item = response.meta['item']
        item['book_price'] = re.findall("\"bp\":'(.*?)',", response.body.decode())
        item['book_price'] = item['book_price'][0] if len(item['book_price']) > 0 else "未查询到价格"
        yield item

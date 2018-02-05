# -*- coding: utf-8 -*-
import scrapy
from book.items import BookItem
import re
from copy import deepcopy
import json


class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']

    def parse(self, response):
        li_list = response.xpath("//ul[@class='ulwrap']/li")  # 大分类的组
        for li in li_list:
            item = BookItem()
            item["b_cate"] = li.xpath("./div[1]/a/text()").extract_first()
            a_list = li.xpath("./div[2]/a")  # 分组获取小分类
            for a in a_list:
                item["s_cate"] = a.xpath("./text()").extract_first()
                item["s_href"] = a.xpath("./@href").extract_first()
                # 请求小分类，到列表页
                if item["s_href"] is not None:
                    item["s_href"] = "http://snbook.suning.com/" + item["s_href"]
                    yield scrapy.Request(
                        item["s_href"],
                        callback=self.parse_book_list,
                        meta={"item": deepcopy(item)}
                    )

    def parse_book_list(self, response):  # 处理列表页
        item = deepcopy(response.meta["item"])
        # item = response.meta["item"]
        li_list = response.xpath("//div[@class='filtrate-books list-filtrate-books']/ul/li")
        for li in li_list:
            item["book_img"] = li.xpath("./div[@class='book-img']//img/@src").extract_first()
            if item["book_img"] is None:
                item["book_img"] = li.xpath("./div[@class='book-img']//img/@src2").extract_first()
            item["title"] = li.xpath(".//div[@class='book-title']/a/@title").extract_first()
            item["book_href"] = li.xpath(".//div[@class='book-title']/a/@href").extract_first()
            item["book_author"] = li.xpath(".//div[@class='book-author']/a/text()").extract_first()
            item["book_press"] = li.xpath(".//div[@class='book-publish']/a/text()").extract_first()
            item["book_desc"] = li.xpath(".//div[@class='book-descrip c6']/text()").extract_first()
            # 请求详情页
            if item["book_href"] is not None:
                yield scrapy.Request(
                    item["book_href"],
                    callback=self.parse_book_detail,
                    meta={"item": deepcopy(item)}
                )
        # 列表页翻页
        '''
        var pagecount=2;
        var currentPage=2;
        '''
        page_count = re.findall("var pagecount=(.*?);", response.body.decode())[0]
        current_page = re.findall("var currentPage=(.*?);", response.body.decode())[0]
        if int(current_page) < int(page_count):
            next_url = item["s_href"] + "?pageNumber={}&sort=0".format(int(current_page) + 1)
            yield scrapy.Request(
                next_url,
                method="POST",
                body=json.dumps({"ajaxFlag": "true"}),  # 需要传一个字符串
                callback=self.parse_book_list,
                meta={"item": response.meta["item"]}  # 必须传，否则调用自己的时候，去meta中的item会报错
                # meta = {"item": item}  # 必须传，否则调用自己的时候，去meta中的item会报错
            )

    def parse_book_detail(self, response):
        item = response.meta["item"]
        # response.body.decode()获取网页的html字符串
        item["book_price"] = re.findall("\"bp\":'(.*?)',", response.body.decode())
        item["book_price"] = item["book_price"][0] if len(item["book_price"]) > 0 else None
        # print(item)
        yield item

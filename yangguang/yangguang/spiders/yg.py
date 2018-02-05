# -*- coding: utf-8 -*-
import scrapy
from yangguang.items import YangguangItem


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):  # 处理列表页
        tr_list = response.xpath("//div[@class='greyframe']/table[2]/tr/td/table/tr")
        for tr in tr_list:
            item = YangguangItem()  # 每次都是一个新的item，所以不会覆盖

            item["num"] = tr.xpath("./td[1]/text()").extract_first()
            item["title"] = tr.xpath("./td[2]/a[2]/@title").extract_first()
            item["href"] = tr.xpath("./td[2]/a[2]/@href").extract_first()
            # print(item)
            # 发送详情页的请求
            yield scrapy.Request(
                item["href"],
                callback=self.parse_detail,
                meta={"item": item}  # 通过meta获取在不同的解析函数中传递数据
            )

        # 发送下一页的请求
        next_url = response.xpath("//a[text()='>']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse  # 下一页的解析方法和当前页面一样
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item["content"] = response.xpath("//div[@class='c1 text14_2']//text()").extract()
        item["content_img"] = response.xpath("//div[@class='c1 text14_2']//img/@src").extract()
        item["content_img"] = ["http://wz.sun0769.com/" + i for i in item["content_img"]]
        # print(item)
        yield item

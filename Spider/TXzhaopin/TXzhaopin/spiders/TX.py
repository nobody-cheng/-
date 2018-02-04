# -*- coding: utf-8 -*-
import scrapy
from TXzhaopin.items import TxzhaopinItem


class TxSpider(scrapy.Spider):
    name = "TX"
    allowed_domains = ["tencent.com"]
    start_urls = (
        'http://hr.tencent.com/position.php',
    )

    def parse(self, response):
        """处理列表页"""
        tr_list = response.xpath(
            "//table[@class='tablelist']//tr[@class='even']|//table[@class='tablelist']//tr[@class='odd']")

        for tr in tr_list:
            print('======================开始for循环==================')
            item = TxzhaopinItem()
            item['job'] = tr.xpath("./td/a/text()").extract_first()
            # 职位类别
            item['Category'] = tr.xpath("./td[2]/text()").extract_first()

            # 招聘人数
            item['num'] = tr.xpath("./td[3]/text()").extract_first()

            # 地址
            item['addr'] = tr.xpath("./td[4]/text()").extract_first()

            # 发布时间
            item['date_time'] = tr.xpath("./td[5]/text()").extract_first()

            # 详情页面
            item['href'] = 'http://hr.tencent.com/' + tr.xpath("./td/a/@href").extract_first()

            # 发送详情页请求
            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={'items': item}  # 通过meta获取在不同的解析函数中传递数据 键可以自己命名
            )

        # 发送下一页请求
        next_url = response.xpath(u"//a[text()='下一页']/@href").extract_first()
        if next_url is not None:
            # 进行拼接url
            next_url = 'http://hr.tencent.com/' + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse  # 下一页的解析方法和当前页面一样
            )

    def parse_detail(self, response):
        item = response.meta['items']

        item['duty'] = response.xpath("//table[@class='tablelist textl']/tr[3]/td/ul//li/text()").extract()
        item['req'] = response.xpath("//table[@class='tablelist textl']/tr[4]/td/ul//li/text()").extract()
        print(item)
        yield item

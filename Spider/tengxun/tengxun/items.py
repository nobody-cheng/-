# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TengxunItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    job = scrapy.Field()
    Category = scrapy.Field()  # 职位类别
    num = scrapy.Field()  # 招聘人数
    addr = scrapy.Field()
    date_time = scrapy.Field()  # 发布时间
    # href = scrapy.Field()  # 详细页面
    duty = scrapy.Field()  # 工作责任
    req = scrapy.Field()  # 工作要求
    detailLink= scrapy.Field() #链接

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    b_class = scrapy.Field()  # 大分类
    c_class = scrapy.Field()  # 小分类
    image = scrapy.Field()  # 图片
    type = scrapy.Field()  # 型号
    num = scrapy.Field()  # 评价人数
    sku = scrapy.Field()  #
    url = scrapy.Field()  #
    price = scrapy.Field()  #
    title = scrapy.Field()  # 书名
    author = scrapy.Field()  # 作者


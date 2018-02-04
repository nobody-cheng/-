# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    b_url = scrapy.Field()  # 大分类地址
    b_title = scrapy.Field()  # 大分类标题
    s_url = scrapy.Field()  # 小分类地址
    s_title = scrapy.Field()  # 小分类标题
    s_filename = scrapy.Field() # 小分类存储路径
    a_url = scrapy.Field() # 小分类里每条新闻连接
    head = scrapy.Field() # 文章标题
    content = scrapy.Field() # 文章内容
    t = scrapy.Field() # 时间
    addr = scrapy.Field() # 来源

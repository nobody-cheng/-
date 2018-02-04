# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    ip = scrapy.Field()  #ip
    port = scrapy.Field() #端口
    style = scrapy.Field() #类型
    addr = scrapy.Field() #地址
    hide =scrapy.Field()  # 隐藏类型
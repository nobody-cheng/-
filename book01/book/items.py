# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    b_cate = scrapy.Field()  #大分类的名字
    s_cate = scrapy.Field() #小分类的名字
    s_href = scrapy.Field()  #小分类的地址
    title = scrapy.Field()  #书名
    book_img = scrapy.Field()  #书的图片
    book_desc = scrapy.Field()  #描述
    book_href = scrapy.Field()
    book_press = scrapy.Field() #出版社
    book_author = scrapy.Field()    #作者
    book_price = scrapy.Field()  #价格


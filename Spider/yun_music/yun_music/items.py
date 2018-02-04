# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YunMusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 大分类 语种
    b_class = scrapy.Field()
    # 小分类 华语,欧美,日语,汉语,粤语
    s_class = scrapy.Field()
    s_href = scrapy.Field()
    # 小分类进来,主题,主题链接,主播,在线听歌人数,
    zhuti = scrapy.Field()
    zhuti_href = scrapy.Field()
    zhubo = scrapy.Field()
    person_num = scrapy.Field()
    # 主题进来歌曲信息,歌曲,时长,歌手,专辑
    song = scrapy.Field()
    time = scrapy.Field()
    singer = scrapy.Field()
    special = scrapy.Field()

    # 列表页下一页
    next_url = scrapy.Field()
    # 歌曲链接
    music_url = scrapy.Field()

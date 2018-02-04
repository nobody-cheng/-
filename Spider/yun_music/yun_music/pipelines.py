# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

i = 1
import json

class YunMusicPipeline(object):
    # def open_spider(self, spider):
    #     client = MongoClient(host=spider.settings['MONGO_HOST'], port=spider.settings['MONGO_PORT'])
    #     self.collection = client['music_wangyi']['music']
    #
    # def process_item(self, item, spider):
    #     global i
    #     i += 1
    #     self.collection.insert_one(dir(item))
    #     print('===============第{}本书=================='.format(i))
    #     return item

    def process_item(self, item, spider):
        global i
        i += 1
        with open('网易云歌单.txt', 'a') as f:
            f.write(json.dumps(dict(item), ensure_ascii=False, indent=2))
            f.write('\n===============第{}次=========\n'.format(i))

        return item

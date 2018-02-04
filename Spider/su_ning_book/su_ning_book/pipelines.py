# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import json

i = 1


class SuNingBookPipeline(object):
    def open_spider(self, spider):
        """定义open_spider和close_spider 一般用于建立数据库的链接和关闭,仅执行一次"""

        client = MongoClient(host=spider.settings["MONGO_HOST"], port=spider.settings["MONGO_PORT"])
        self.collection = client['suning']['book']

    def process_item(self, item, spider):
        global i
        i+=1
        self.collection.insert_one(dict(item))  # 插入数据
        print('===============第{}本书=================='.format(i))
        return item


        # def process_item(self, item, spider):
        #     global i
        #     i += 1
        #     with open('book.txt', 'a') as f:
        #         f.write(json.dumps(dict(item), ensure_ascii=False, indent=2))
        #         f.write('\n===============第{}次=========\n'.format(i))
        #         print('===============第{}次========='.format(i))
        #     return item

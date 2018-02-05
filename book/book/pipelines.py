# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class BookPipeline(object):
    def open_spider(self,spider):
        client = MongoClient(host=spider.settings["MONGO_HOST"],port=spider.settings["MONGO_PORT"])
        self.collection = client["book"]["suning"]

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item)) #插入数据
        return item

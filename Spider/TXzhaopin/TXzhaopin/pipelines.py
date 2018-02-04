# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import re

client = MongoClient(host='127.0.0.1', port=27017)
collection = client['TXzhaopin']['zhaopin']


class TxzhaopinPipeline(object):
    def process_item(self, item, spider):
        self.process_item_contents(item['duty'])
        self.process_item_contents(item['req'])
        collection.insert_one(dict(item))
        print('hello scrapy')
        return item

    def process_item_contents(self, contents_list):
        contents_list = [re.sub(r"\xa0|\s+", '', i) for i in contents_list]

        contents_list = [i for i in contents_list if len(i) > 0]
        return contents_list

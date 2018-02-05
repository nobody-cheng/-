# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from pymongo import MongoClient

client = MongoClient(host="127.0.0.1", port=27017)
collection = client["spider"]["yangguang"]


class YangguangPipeline(object):
    def process_item(self, item, spider):
        item["content"] = self.process_item_content(item["content"])
        print(item)
        collection.insert_one(dict(item))  # 使用dict把item转化为字典
        return item

    def process_item_content(self, content_list):  # 处理content字段的值
        content_list = [re.sub(r"\xa0|\s+", "", i) for i in content_list]  # 把不要的字符串替换成空字符串
        content_list = [i for i in content_list if len(i) > 0]  # 不要空字符串
        return content_list

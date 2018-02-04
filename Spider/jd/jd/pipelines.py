# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import json

i = 1


class JdPipeline(object):
    def process_item(self, item, spider):
        # item["crawled"] = datetime.utcnow()
        # item["spider"] = spider.name
        return item

        # def process_item(self, item, spider):
        #     global i
        #     i += 1
        #     with open('京东笔记本.txt', 'a') as f:
        #         f.write(json.dumps(dict(item), ensure_ascii=False, indent=2))
        #         f.write('\n===============第{}次=========\n'.format(i))

        # return item

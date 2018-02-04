# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

i = 1


class TengxunPipeline(object):
    # def process_item(self, item, spider):
    #     return item

    def process_item(self, temp, spider):
        global i
        i += 1
        with open('job.txt', 'a') as f:
            f.write(json.dumps(dict(temp), ensure_ascii=False, indent=2))
            f.write('\n===============第{}条=========\n'.format(i))
            print('===============第{}次========='.format(i))
        return temp

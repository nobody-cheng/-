# -*- coding: utf-8 -*-
import scrapy
import os
from sina.items import SinaItem


class SinaSpiderSpider(scrapy.Spider):
    name = 'sina_spider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        items = []
        # 所有大类的url 和 标题
        b_url = response.xpath("//div[@id='tab01']/div/h3/a/@href").extract()
        b_title = response.xpath("//div[@id='tab01']/div/h3/a/text()").extract()

        # s所有小类的url和标题
        s_url = response.xpath("//div[@id='tab01']/div/ul/li/a/@href").extract()
        s_title = response.xpath("//div[@id='tab01']/div/ul/li/a/text()").extract()

        # 爬所有大类
        for i in range(0, len(b_url)):
            # 指定大类目录的路径和目录名
            b_filename = './data/' + b_title[i]

            # 目录不存在,创建目录
            if not os.path.exists(b_filename):
                os.makedirs(b_filename)
            # 爬小分类
            for j in range(0, len(s_url)):
                item = SinaItem()
                item['b_url'] = b_url[i]
                item['b_title'] = b_title[i]

                # 检查小类的url是否以同类别大类url开头，如果是返回True (sports.sina.com.cn 和 sports.sina.com.cn/nba)
                if_belong = s_url[j].startswith(item['b_url'])
                if if_belong:
                    s_filename = b_filename + '/' + s_title[j]
                    # 目录不存在,创建目录
                    if not os.path.exists(s_filename):
                        os.makedirs(s_filename)
                        # 存储小类url,title,s_filename字段数据
                    item['s_url'] = s_url[j]
                    item['s_title'] = s_title[j]
                    item['s_filename'] = s_filename
                    items.append(item)
            # 发送每个小类url的Request请求，得到Response连同包含meta数据 一同交给回调函数 second_parse 方法处理
            for item in items:
                yield scrapy.Request(
                    url=item['s_url'],
                    callback=self.second_parse,
                    meta={'meta_1': item}
                )

    def second_parse(self, response):
        meta_1 = response.meta['meta_1']
        # 取出小类里所有子链接
        a_url = response.xpath("//a/@href").extract()
        items = []
        for i in range(0, len(a_url)):
            # 检查每个链接是否以大类url开头、以.shtml结尾，如果是返回True
            if_belong = a_url[i].endswith('.shtml') and a_url[i].startswith(meta_1['b_url'])
            # 如果属于本大类，获取字段值放在同一个item下便于传输
            if if_belong:
                item = SinaItem()
                item['b_url'] = meta_1['b_url']
                item['b_title'] = meta_1['b_title']
                item['s_title'] = meta_1['s_title']
                item['s_url'] = meta_1['s_url']
                item['s_filename'] = meta_1['s_filename']
                item['a_url'] = a_url[i]
                items.append(item)
        for item in items:
            yield scrapy.Request(
                url=item['a_url'],
                callback=self.detail_parse,
                meta={'meta_2': item}
            )

    def detail_parse(self, response):
        item = response.meta['meta_2']
        content = ''
        # id = artibodyTitle
        head = response.xpath("//h1[@class='main-title']/text()").extract_first()
        if head is None:
            head = response.xpath("//h1[@id='artibodyTitle']/text()").extract_first()
        content_list = response.xpath("//div[@id='artibody']/p/text()").extract()

        # 将p标签里的文本内容合并到一起
        for content_one in content_list:
            content += content_one
        item['head'] = head
        item['content'] = content.split()

        yield item

        """页面的标题和文本内容的标签有出入需要重新整理"""

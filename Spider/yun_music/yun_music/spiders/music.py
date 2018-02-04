# -*- coding: utf-8 -*-
import scrapy
from yun_music.items import YunMusicItem
from copy import deepcopy
from selenium import webdriver

i = 1


class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/discover/playlist']

    def parse(self, response):
        """处理数据和提取url"""
        print('*' * 100)
        dl_list = response.xpath("//div[@class='bd']/dl")  # 得到5个大分类对象
        for dl in dl_list:
            item = YunMusicItem()
            item['b_class'] = dl.xpath("./dt/text()").extract_first() if len(dl.xpath("./dt/text()")) > 0 else None

            dd_list = dl.xpath("./dd/a")  # 语种分类对象  华语,欧美,日语,汉语,粤语
            for dd in dd_list:
                item['s_class'] = dd.xpath("./text()").extract_first() if len(dd.xpath("./text()")) > 0 else '未取到语种分类'
                item['s_href'] = "http://music.163.com" + dd.xpath("./@href").extract_first() if len(
                    dd.xpath("./@href")) > 0 else '未取到语种链接'

                if item['s_href'] is not None:
                    yield scrapy.Request(
                        item['s_href'],
                        self.get_play_list,
                        meta={'item': deepcopy(item)}
                    )

    def get_play_list(self, response):
        """每一分类的列表页面"""
        item = response.meta['item']
        li_list = response.xpath(".//ul[@class='m-cvrlst f-cb']//li")
        # 对每一个主题进行遍历  主题,主题链接,主播,在线听歌人数
        for li in li_list:
            item['zhuti'] = li.xpath("./p[1]/a/text()").extract_first() if len(
                li.xpath("./p[1]/a/text()")) > 0 else '未找到主题'
            item['zhuti_href'] = "http://music.163.com" + li.xpath("./p[1]/a/@href").extract_first() if len(
                li.xpath("./p[1]/a/@href")) > 0 else '未找到主题链接'
            item['zhubo'] = li.xpath("./p[2]/a/text()").extract_first() if len(
                li.xpath("./p[2]/a/text()")) > 0 else '未找到主播'
            item['person_num'] = li.xpath("./div/div/span[2]/text()").extract_first() if len(
                li.xpath("./div/div/span[2]/text()")) > 0 else '暂无在线听歌'
            # 请求详情页信息 歌单

            if item['zhuti_href'] is not None:
                yield scrapy.Request(
                    item['zhuti_href'],
                    self.get_music_list,
                    meta={'item': deepcopy(item)}
                )
        # 列表翻页
        item['next_url'] = "http://music.163.com" + response.xpath("//a[text()='下一页']/@href").extract_first() if len(
            response.xpath("//a[text()='下一页']/@href")) > 0 else '最后一页'
        if item['next_url'] is not None:
            yield scrapy.Request(
                item['next_url'],
                self.get_play_list,
                meta={'item': item}  # 改item必须传,否则递归时候response无meta,会在response.meta['item']报错
            )

    # 该种方法太慢
    # def get_music_list(self, response):
    #     """歌单详情页---动态页面"""
    #     item = response.meta['item']
    #     url = item['zhuti_href']
    #     driver = webdriver.Chrome()
    #     driver.get(url)
    #     # 如果iframe标签有id时，切换iframe时把id作为参数直接传入
    #     driver.switch_to.frame('g_iframe')
    #     tr_list = driver.find_elements_by_xpath("//tbody/tr")
    #     for tr in tr_list:
    #         item['song'] = tr.find_element_by_xpath("./td[2]//b").get_attribute('title')
    #         item['time'] = tr.find_element_by_xpath("./td[3]/span").text
    #         item['singer'] = tr.find_element_by_xpath("./td[4]/div").get_attribute('title')
    #         item['special'] = tr.find_element_by_xpath("./td[5]//a").get_attribute('title')
    #         yield item

    def get_music_list(self, response):
        """歌单详情页---动态页面"""
        item = response.meta['item']
        # 获取到歌单每条歌曲的链接
        li_list = response.xpath(".//div[@id='song-list-pre-cache']/ul/li")
        for li in li_list:
            item['music_url'] = "http://music.163.com" + li.xpath("./a/@href").extract_first() if len(
                li.xpath("./a/@href")) else '无歌曲链接'
            item['song'] = li.xpath("./a/text()").extract_first() if len(li.xpath("./a/text()")) else '无歌曲名'

            # 请求歌曲详情
            if item['music_url'] is not None:
                yield scrapy.Request(
                    item['music_url'],
                    self.get_music_info,
                    meta={'item': deepcopy(item)}
                )

    def get_music_info(self, response):
        """歌曲详情页"""
        item = response.meta['item']
        info_list = response.xpath(".//script[@type='application/ld+json']/text()").extract_first() if len(
            response.xpath(".//script[@type='application/ld+json']/text()")) > 0 else '网页不同'
        '''
        {
            "@context": "https://ziyuan.baidu.com/contexts/cambrian.jsonld",
            "@id": "http://music.163.com/song?id=511680246",
            "appid": "1582028769404989",
            "title": "AMANI",
            "images": ["http://p1.music.126.net/d3PmE2elBjkTHrjEqo2KWg==/109951163039027386.jpg"],
            "description": "歌手：Newyounggoswag。所属专辑：AMANI。",
            "pubDate": "2017-10-08T03:09:06"
        }'''
        if info_list == '网页不同':
            item['singer'] = '网页不同'
            item['special'] = '网页不同'

        info_dict = eval(info_list)
        item['singer'] = info_dict['description'].split('。')[0][3:]
        item['special'] = info_dict['description'].split('。')[1][5:-1]
        global i

        print('*********************第{}首歌曲******************'.format(i))
        print(item)
        i += 1
        yield item

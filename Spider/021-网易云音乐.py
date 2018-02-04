from selenium import webdriver
from retrying import retry
from lxml import etree
import time
import re
import requests
from queue import Queue


class wangyimusicSpider():
    def __init__(self):
        self.url = 'http://music.163.com/discover/playlist'
        self.header_url = 'http://music.163.com/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"
        }

        self.url_temp = Queue()
        self.html_str_queue = Queue()
        self.content_list_queue = Queue()

        with open("test.csv", "w", encoding="utf-8") as f:  # 设置csv的第一行的数据
            f.write("歌单,主播,歌曲,歌手,专辑,发行时间" + "\n")



    @retry(stop_max_attempt_number=5)
    def _parse_url(self, url):

        html_str = requests.get(url, headers=self.headers, timeout=5)
        return html_str.content.decode()

    def parse_url(self, url):
        """请求地址,返回json数据"""
        try:
            html_str = self._parse_url(url)
        except Exception as e:
            html_str = None
            print('请求错误信息', e)
        return html_str

    def get_contents(self, html_str):
        """获取歌单封面信息"""
        print('开始提取数据')
        html_str = re.sub(r'<!--|-->', '', html_str)
        # print(html_str)
        html = etree.HTML(html_str)
        # 得到歌单对象
        li_list = html.xpath(".//ul[@class='m-cvrlst f-cb']/li")

        # 分组,进行遍历得到所有歌单列表
        content_list = []
        for li in li_list:
            item = {}
            item['歌单'] = li.xpath(".//a[@class='msk']/@title")[0] if len(
                li.xpath(".//a[@class='msk']/@title")) else "无歌单"
            item['主播'] = li.xpath(".//a[@class='nm nm-icn f-thide s-fc3']/@title")[0] if len(
                li.xpath(".//a[@class='nm nm-icn f-thide s-fc3']/@title")) > 0 else '暂无主播'
            item['在线人数'] = li.xpath(".//span[@class='nb']/text()")[0] if len(
                li.xpath(".//span[@class='nb']/text()")) else '暂无人收听,人气不足'
            # 歌单链接
            music_url = li.xpath(".//a[@class='tit f-thide s-fc0']/@href")[0] if len(
                li.xpath(".//a[@class='tit f-thide s-fc0']/@href")) > 0 else '无歌单链接,请重试'
            music_url = self.header_url + music_url
            print('*' * 100)
            # 获取歌曲的详细信息
            item['歌曲信息'] = self.get_music_info(music_url)

            content_list.append(item)

            self.save_data(content_list)

        next_url = html.xpath("//a[text()='下一页']/@href")
        if len(next_url) > 0:
            next_url = self.header_url + next_url[0]
        else:
            next_url = None

        return content_list, next_url

    def get_music_info(self, li_url):
        """获取歌单详情页内容"""
        if li_url is not None:
            # 请求歌单详情的地址
            info_html = self.parse_url(li_url)
            info_html_list = etree.HTML(info_html)
            music_info_list = info_html_list.xpath(".//div[@id='song-list-pre-cache']/ul/li")

            info_list = []
            for info in music_info_list:
                item = {}
                item['歌曲'] = info.xpath(".//a/text()")[0]
                music_url = self.header_url + info.xpath(".//a/@href")[0]
                music_info = self.music_info(music_url)
                item['发行时间'] = music_info['发行时间']
                item['所属专辑'] = music_info['所属专辑']
                item['歌手'] = music_info['歌手']
                info_list.append(item)

            return info_list

        return None

    def music_info(self, url):
        print('提取歌曲详情信息')
        html_str = self.parse_url(url)
        html = etree.HTML(html_str)

        try:
            info = html.xpath(".//script[@type='application/ld+json']/text()")[0].replace("space", "")
        except Exception as e:
            info = None
            print('歌曲详单信息错误:', e)

        info_dict = eval(info)
        info_item = {}
        info_item['歌手'] = info_dict['description'].split('。')[0][3:]
        info_item['所属专辑'] = info_dict['description'].split('。')[1][5:]
        info_item['发行时间'] = info_dict['pubDate'][0:10]

        return info_item

    def save_data(self, content_list):
        print('$' * 100)
        for content in content_list:
            text_list = content['歌曲信息']
            gedan = content['歌单']
            zhubo = content['主播']
            for text in text_list:

                temp_list = [gedan, zhubo, text['歌曲'], text['歌手'], text['所属专辑'],
                             text['发行时间']]
                temp_str = ",".join([str(i) for i in temp_list]) + "\n"
                print(temp_str)

                with open('{}{}{}.csv'.format(content['歌单'], content['主播'], content['在线人数']), 'a',
                          encoding='utf-8') as f:
                    f.write(temp_str)

    def run(self):
        """主逻辑"""
        next_url = self.url
        i = 1
        while next_url is not None:
            print('第{}页歌曲'.format(i))
            i += 1
            # 1.获取url
            # 2.请求url,返回数据
            html_str = self.parse_url(next_url)
            # 3.提取整理数据
            content_list, next_url = self.get_contents(html_str)

            # 4.保存
            # self.save_data(content_list)


if __name__ == '__main__':
    wymusic = wangyimusicSpider()
    wymusic.run()

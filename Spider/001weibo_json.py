import json
import requests
import re
from retrying import retry
import random
import time
import urllib.request
import os

index = 1


class weiboSpider():
    def __init__(self):
        # self.url = 'https://m.weibo.cn/api/container/getIndex?uid=1223178222&luicode=10000011&lfid=100103type=1&' \
        #            'q=%E8%83%A1%E6%AD%8C&featurecode=20000320&type=uid&value=1223178222&containerid=1076031223178222' \
        #            '&page=4'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 "
                          "(KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
            "Host": "m.weibo.cn",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
        }
        self.imgPath = r'/home/python/Desktop/python/image'

    @retry(stop_max_attempt_number=5)
    def _parse_url(self, url):
        response = requests.get(url, headers=self.headers, timeout=5)
        return response.json()

    def parse_url(self, url):
        """发送请求"""
        try:
            html_str = self._parse_url(url)
        except Exception as e:
            print('请求失败:', e)
            html_str = None
        return str(html_str)

    def get_content_list(self, html_str):
        """提取图片url地址数据"""
        url1 = r'https.*?\''
        url_list = re.findall(url1, html_str)
        key = 'large'
        urls = []
        for image_url in url_list:
            if key in image_url:
                urls.append(image_url)
        return urls

    def download(self, image_urls):
        if not os.path.isdir(self.imgPath):
            os.mkdir(self.imgPath)
        global index
        for url in image_urls:
            print("下载:", url)
            try:
                res = urllib.request.urlopen(url)
                if str(res.status) != '200':
                    print('未下载成功：', url)
                    continue
            except Exception as e:
                print('错误原因:', e)
                print('未下载成功：', url)

            filename = os.path.join(self.imgPath, str(index) + '.jpg')
            with open(filename, 'wb') as f:
                f.write(res.read())
                print('下载完成\n')
                index += 1

    def run(self):
        # 实现主要逻辑
        i = 1
        while True:
            time.sleep(random.randint(4, 8))
            print(random.randint(4, 8))
            url = 'https://m.weibo.cn/api/container/getIndex?uid=1223178222&luicode=10000011&lfid=100103type=1&q=%E8%83%A1%E6%AD%8C' \
                  '&featurecode=20000320&type=uid&value=1223178222&containerid=1076031223178222&page={}'.format(i)
            i += 1
            html_str = self.parse_url(url)
            urls = self.get_content_list(html_str)
            print(urls)

            self.download(urls)


if __name__ == '__main__':
    weibo = weiboSpider()
    weibo.run()

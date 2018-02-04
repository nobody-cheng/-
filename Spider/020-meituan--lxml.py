"""
http://hotel.meituan.com/shenzhen/
http://hotel.meituan.com/guangzhou/
"""
import requests
from retrying import retry
from lxml import etree
import time
import re


class meituanSpider():
    def __init__(self, name):
        self.url = 'http://hotel.meituan.com/{}/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3"
                          "202.94 Safari"
        }
        self.city = name


    def get_url(self):
        url = self.url.format(self.city)
        return url

    @retry(stop_max_attempt_number=5)
    def _parse_url(self, url):
        html_json = requests.get(url, headers=self.headers, timeout=5)
        return html_json.content.decode()

    def parse_url(self, url):
        try:
            html_str = self._parse_url(url)
        except Exception as e:
            html_str = None
            print('请求错误信息', e)
        return html_str

    def get_contents_list(self, html_str):
        print('进行提取数据')
        html_str = re.sub(r'<!--|-->', '', html_str)
        # 创建xpath对象
        html = etree.HTML(html_str)
        # 分组
        div_list = html.xpath(".//div[@class='poi-results']//article")
        # print(div_list)
        # 进行遍历得到所有酒店
        content_list = []
        for div in div_list:
            print(div)
            item = {}
            item['酒店'] = div.xpath(".//div[@class='info-wrapper']/h3/a/text()")[0] if len(
                div.xpath(".//div[@class='info-wrapper']/h3/a/text()")) > 0 else '未查询到'
            print('酒店==', item['酒店'])
            item['地址'] = div.xpath(".//div[@class='poi-address']/text()")[0].strip() if len(
                div.xpath(".//div[@class='poi-address']/text()")) else '未获取到地址'
            print('地址==', item['地址'])
            item['评分'] = div.xpath(".//div[@class='poi-grade']/text()")[0].strip() if len(
                div.xpath(".//div[@class='poi-grade']/text()")) > 0 else '暂无评分'
            # print('评分==', item['评分'])
            item['评价'] = div.xpath(".//span[@class='poi-grade-desc']/text()")[0] if len(
                div.xpath(".//span[@class='poi-grade-desc']/text()")) else '暂无评价'
            # print('评价==', item['评价'])
            item['价格'] = (div.xpath(".//div[@class='poi-price']/em/text()")[0] + '元起') if len(
                div.xpath(".//div[@class='poi-price']/em/text()")) else '暂无价格'
            # print('价格==', item['价格'])
            item['设施'] = div.xpath(".//img/@title")
            print('设施==', item['设施'])





            content_list.append(item)
    # 提取下一页


    def save_data(self):
        pass

    def run(self):
        # 1.获取url
        url = self.get_url()
        # print('......', url)
        # 2.请求url,返回数据
        html_str = self.parse_url(url)
        # 3.提取整理数据
        self.get_contents_list(html_str)
        # 4.保存


if __name__ == '__main__':
    # meituan = meituanSpider(input('请输入需要爬取的城市酒店信息:'))
    meituan = meituanSpider('shenzhen')
    meituan.run()

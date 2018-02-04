"""爬取所选贴吧的页面主题,主题链接,帖子图片"""
import requests
from retrying import retry
from lxml import etree
import re
import time
import random


class tiebaSpider():
    def __init__(self, tieba_name):
        self.url = "https://tieba.baidu.com/f?ie=utf-8&kw={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202."
                          "94 Safari/537.36"
        }
        self.tieba_name = tieba_name

    def get_url(self):
        """获取需要爬取的贴吧"""
        url = self.url.format(self.tieba_name)
        return url

    @retry(stop_max_attempt_number=5)
    def _parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def parse_url(self, url):
        try:
            html_str = self._parse_url(url)
        except Exception as e:
            html_str = None
            print("请求错误", e)
        return html_str

    def get_contents_list(self, html_str):
        """提取列表页面主题及链接信息"""
        print("提取数据")
        # print(type(html_str))
        # 创建xpath对象
        html_str = re.sub(r'<!--|-->', '', html_str)
        html = etree.HTML(html_str)

        # 分组
        div_list = html.xpath(".//div[@class='threadlist_title pull_left j_th_tit ']/a")
        # print(div_list)
        content_list = []
        for div in div_list:
            """对每一个主题进行遍历"""
            print("遍历帖子")
            item = {}
            # print('div==', div)
            # 提取主题 if len(
            item["title"] = div.xpath(".//@title")[0] if len(div.xpath(".//@title")[0]) > 0 else "无主题"
            # print(len(div.xpath(".//@title")[0]))
            # 提取链接
            item["href"] = "https://tieba.baidu.com" + div.xpath(".//@href")[0] if len(
                div.xpath(".//@href")[0]) > 0 else "无链接"
            # 提取帖子里面的图片
            item["img_list"] = self.get_images(item["href"], [])
            content_list.append(item)
        # print(content_list)
        # 提取下一页
        next_url = html.xpath(".//a[@class='next pagination-item ']/@href")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxx", next_url)
        if next_url is not None:
            next_url = "https:" + next_url[0]
            print("下一页地址", next_url)
        else:
            next_url = None
        return content_list, next_url

    def get_images(self, detail_url, total_img_list):
        if detail_url is not None:
            print("提取图片")
            # 请求帖子内容
            # print(detail_url)
            html_str = self.parse_url(detail_url)
            # html_str = re.sub(r'<!--|-->', '', html_str)
            detail_html = etree.HTML(html_str)
            # 获取到当前页面所有帖子正文图片
            image_list = detail_html.xpath(".//img[@class='BDE_Image']/@src")
            total_img_list += image_list
            # 获取帖子下一页的链接
            detail_next_url = detail_html.xpath("//a[text()='下一页']/@href")

            # 判断是否有下一页,根据href长度,再循环--请求帖子内容--获取到当前页面所有帖子正文图片--获取帖子下一页的链接
            if len(detail_next_url) > 0:
                # 构建下一页地址
                detail_next_url = "https://tieba.baidu.com" + detail_next_url[0]
                return self.get_images(detail_next_url, total_img_list)
            else:
                return total_img_list
        else:
            return total_img_list  # 空

    def save_data(self, content_list):
        for content in content_list:
            print(content)
        print("===================保存成功===================")

    def run(self):
        """主逻辑"""
        # 获取url地址
        next_url = self.get_url()
        i = 1
        while next_url is not None:
            print("第%s页" % i)
            i += 1
            # 请求返回json数据
            html_str = self.parse_url(next_url)
            # 请求下一页的URL地址
            content_list, next_url = self.get_contents_list(html_str)
            # 保存数据
            self.save_data(content_list)
            t = random.randint(1, 5)
            time.sleep(t)


if __name__ == '__main__':
    tieba = tiebaSpider(input("请输入需要爬取的贴吧:"))
    # tieba = tiebaSpider('皇家马德里')
    tieba.run()

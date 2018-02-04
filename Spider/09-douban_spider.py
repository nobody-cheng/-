import requests
import re
import json

"""
1.url地址
2.请求url
3.返回json数据,转为python数据类型
4.提取数据,电视剧名,导演,评分
"""


class Movie():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3"
                          "202.94 Safari"
        }
        self.url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_domestic_hot/items?os=ios&for_mobi" \
                   "le=0&start={}&count=50&loc_id=108288&_=0"

    def get_url_list(self):
        url_list = {self.url.format(i * 50) for i in range(0, 9)}
        # print(url_list)
        return url_list

    def parse_url(self, url):
        """发送请求,获取数据"""
        ret = requests.get(url)
        html_str = ret.content.decode()
        return html_str

    def handle_data(self, html_str):
        """处理浏览器返回的数据"""
        # 转为python类字典
        html_dict = json.loads(html_str)
        # 转为json数据
        html_dict = json.dumps(html_dict, ensure_ascii=False, indent=2)

        with open("douban.html", "a", encoding="utf-8") as f:
            f.write(html_dict)
            i = 1
            print("handle_data")
        return "ok"

    def get_movies_info(self):
        """获取电视剧信息"""
        html = open('douban.html', encoding="utf-8").read()

        title = re.findall('"title": "(.*)",', html)
        return title

    def run(self):
        # 1.获取所有的url列表
        url_list = self.get_url_list()
        # 2.遍历url_list,请求url
        for i, url in enumerate(url_list):
            print(i)
            html_str = self.parse_url(url)
            # 3.处理浏览器返回的数据
            self.handle_data(html_str)

    def get_info(self):
        """4.提取数据, 电视剧名, 导演, 评分"""

        titles = self.get_movies_info()
        title = str(set(titles))

        with open("tv.txt", 'w', encoding="utf-8")as f:
            f.write(title)
        print("共找到%s部电影" % len(set(titles)))


if __name__ == '__main__':
    movie = Movie()
    movie.run()
    movie.get_info()

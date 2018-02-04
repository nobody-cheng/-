"""
http://www.neihan8.com/article/list_5_1.html
http://www.neihan8.com/article/list_5_2.html
http://www.neihan8.com/article/list_5_3.html

<a href="/article/45024.html">老师，你脱光衣服我照样认识你！</a></h4>
<div class="f18 mb20"><p>小明妈带着幼儿园的小明到女澡堂洗澡，进去看到了老师也在洗，老师装做不认识小明，<br />
快步走进淋浴间。小明大喊:老师！老师，你脱光衣服我照样认识你~</p></div>
re.findall(r'<a\shref="/article/\d+\.html">(.*?)</a>.*?<div\sclass="f18 mb20"><p>(.*?)</p></div>',re.S)  不包含外侧双引号
"""

import requests
import re


class Neihan():
    def __init__(self):
        self.url = "http://www.neihan8.com/article/list_5_{}.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3"
                          "202.94 Safari"
        }

    def url_lists(self, i):
        """获取url"""
        url_list = self.url.format(i)
        return url_list

    def parse_url(self, url):
        """请求url,获取json数据"""
        response = requests.get(url, headers=self.headers, timeout=2)
        if response.status_code == 200:
            return response.content.decode("gbk")
        else:
            raise ValueError("status_code is:", response.status_code)

    def get_content(self, str):
        """提取数据"""
        print(str)
        # ======================================
        pattern = re.compile(r'<a\shref="/article/\d+\.html">(.*?)</a>.*?<div\sclass="f18 mb20">(.*?)'
                             r'</div>', re.S)  # \s 空白符; re.S 不包含外侧双引号
        t = pattern.findall(str)
        # =======================================
        print(t)

        result = []
        for i in t:
            temp = []
            for j in i:
                j = re.sub(r"[<b>|</b>|<br />|<br>|<p>|</p>|\\u3000|\\r\\n|\s]", "", j)

    def run(self):
        i = 1
        while i <= 1:
            # 1.获取所有要爬取的url
            url = self.url_lists(i)
            # 2.请求url,返回数据
            json_str = self.parse_url(url)
            # 3.数据整理提取
            ret = self.get_content(json_str)
            i += 1


if __name__ == '__main__':
    neihan = Neihan()
    neihan.run()

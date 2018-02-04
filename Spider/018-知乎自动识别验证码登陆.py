import requests
from lxml import etree
from retrying import retry
import time
from yundama.dama import indetify


class zhihuSpider():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3"
                          "202.94 Safari"
        }
        self.url = 'https://www.zhihu.com/#signin'
        self.session = requests.session()
        self.captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)

    @retry(stop_max_attempt_number=5)
    def _parse_url(self, url):
        response = self.session.get(url, headers=self.headers, timeout=5)
        return response.content.decode()

    def parse_url(self, url):
        try:
            html_str = self._parse_url(url)

        except Exception as e:
            html_str = None
            print(e)
        return html_str

    def get_content(self, html_str):
        try:
            print('aaaaaaaaaaaaaa', html_str)
            html = etree.HTML(html_str)
        except Exception as e:
            print('html节点错误:', e)
            html = None
        return html

    def login(self, html):
        _xsrf = html.xpath("//input[@name='_xsrf']/@value")[0]
        # 验证码url地址
        captcha_url = self.captcha_url
        captcha_response = self.session.get(captcha_url, headers=self.headers)
        with open('temp.gif', 'wb')as f:
            f.write(captcha_response.content)
        captcha = indetify(captcha_response.content)
        post_data = {
            "_xsrf": _xsrf,
            "email": "13823875990",
            "password": "zc19900126",
            "remember_me": True,
            "captcha": captcha
        }
        resp = self.session.post('https://www.zhihu.com/login/email', data=post_data, headers=self.headers)
        # print(resp.status_code)
        # print(resp.content.decode())
        resposne = self.session.get("https://www.zhihu.com/", headers=self.headers)

        with open('login.html', 'w', encoding='utf-8')as f:
            f.write(resposne.content.decode())

    def save_data(self):
        print('保存成功')

    def run(self):
        """主逻辑"""
        # 1.获取url
        url = self.url

        # 2.请求url,获取响应
        response = self.parse_url(url)

        # 3.提取整理数据
        html = self.get_content(response)
        # 4.登陆
        self.login(html)
        # 5.保存数据
        self.save_data()


if __name__ == '__main__':
    zhihu = zhihuSpider()
    zhihu.run()
"""未完成"""

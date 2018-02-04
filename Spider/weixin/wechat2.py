import json
import requests
import re
import random
import time
from header import chiose_user_agent

wechat_list = ['庞门正道', 'Python之美']


class WeiXin(object):
    def __init__(self, cookies):
        self.login_url = 'https://mp.weixin.qq.com/'
        self.header = {
            "User-Agent": chiose_user_agent.get_ua()
        }
        self.cookies = cookies

    def get_token(self):
        response = requests.get(url=self.login_url, cookies=self.cookies)
        print(response.url)
        token = re.findall(r'token=(\d+)', str(response.url))[0]
        return token

    def get_search(self, token, wechat):
        # 搜索微信公众号的接口地址
        search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
        # token,随机数(0,1),query>公众号
        get_data = {
            'action': 'search_biz',
            'token': token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': 1,
            'random': random.random(),
            'query': wechat,
            'begin': 0,
            'count': 5
        }
        # 打开搜索的微信公众号文章列表页
        search_response = requests.get(search_url, headers=self.header, cookies=self.cookies, params=get_data)
        # print(search_response.json().get('list')[0])
        lists = search_response.json().get('list')[0]

        # 获取这个公众号的fakeid，后面爬取公众号文章需要此字段
        fakeid = lists.get('fakeid')
        return fakeid

    def get_content(self, token, fakeid,begin):
        detail = {}
        # 微信公众号文章接口地址
        appmsg_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
        get_data1 = {
            'token': token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'random': random.random(),
            'action': 'list_ex',
            'begin': '{}'.format(begin),  # 不同页，此参数变化，变化规则为每页加5
            'count': '5',
            'query': '',
            'fakeid': fakeid,
            'type': '9'
        }
        appmsg_response = requests.get(appmsg_url, cookies=self.cookies, headers=self.header, params=get_data1)
        # 获取文章总数
        max_num = appmsg_response.json().get('app_msg_cnt')
        content_list = appmsg_response.json().get('app_msg_list')
        for content in content_list:
            detail['link'] = content.get('link')
            detail['title'] = content.get('title')

        num = int(int(max_num / 5))
        return detail, num

    def run(self, wechat):
        # 获取token
        token = self.get_token()
        # 获取每个公众号的faked
        fakeid = self.get_search(token, wechat)
        begin = 0

        item, num = self.get_content(token, fakeid, begin)

        while num + 1 > 0:
            print('正在翻页：--------------', begin)
            item, num = self.get_content(token, fakeid, begin)
            num -= 1
            begin = int(begin)
            begin += 5
            time.sleep(random.randint(3, 7))
            print(item)


if __name__ == '__main__':
    with open('cookie.txt', 'r', encoding='utf-8') as f:
        cookie = f.read()
    cookies = json.loads(cookie)
    weixin = WeiXin(cookies)
    for wechat in wechat_list:
        weixin.run(wechat)

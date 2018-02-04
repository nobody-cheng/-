import json
import requests
import re
import random
import time

login_url = 'https://mp.weixin.qq.com/'
# wechat_list = ['庞门正道']
wechat_list = ['庞门正道']


def get_weixin(wechat):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
    }
    with open('cookie.txt', 'r', encoding='utf-8') as f:
        cookie = f.read()
    cookies = json.loads(cookie)
    response = requests.get(url=login_url, cookies=cookies)
    print(response.url)
    token = re.findall(r'token=(\d+)', str(response.url))[0]

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
    search_response = requests.get(search_url, headers=header, cookies=cookies, params=get_data)
    # print(search_response.json().get('list')[0])
    lists = search_response.json().get('list')[0]

    # 获取这个公众号的fakeid，后面爬取公众号文章需要此字段
    fakeid = lists.get('fakeid')

    # 微信公众号文章接口地址
    appmsg_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
    get_data1 = {
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'action': 'list_ex',
        'begin': '0',  # 不同页，此参数变化，变化规则为每页加5
        'count': '5',
        'query': '',
        'fakeid': fakeid,
        'type': '9'
    }
    appmsg_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=get_data1)
    # 获取文章总数
    max_num = appmsg_response.json().get('app_msg_cnt')
    print(max_num)
    print(type(int(max_num)))
    num = int(max_num) / 5
    begin = 0
    while num + 1 > 0:
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
        print('正在翻页：--------------', begin)
        response = requests.get(appmsg_url, cookies=cookies, headers=header, params=get_data1)
        content_list = response.json().get('app_msg_list')
        for content in content_list:
            link = content.get('link')
            title = content.get('title')
            file_name = wechat + '.txt'
            with open(file_name, 'a', encoding='utf-8') as f:
                f.write(title + ':\n' + link + '\n')
        num -= 1
        begin = int(begin)
        begin += 5
        time.sleep(random.randint(5, 10))


if __name__ == '__main__':

    for wechat in wechat_list:
        get_weixin(wechat)

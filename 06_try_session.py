# coding=utf-8
import requests
import re

profile_url = "http://www.renren.com/327550029/profile"
post_url = "http://www.renren.com/PLogin.do"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
post_data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}

session = requests.session()  #实例化session
session.post(post_url,headers=headers,data=post_data) #请求post的地址，对方服务器在session中设置cookie

response = session.get(profile_url,headers=headers) #访问个人主页

print(re.findall("你瞅啥",response.content.decode())) #查看用户名是否在响应中


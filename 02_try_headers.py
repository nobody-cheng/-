# coding=utf-8
import requests
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
url = "http://www.baidu.com"
response = requests.get(url,headers=headers)
print(response.content.decode())


# coding=utf-8
import requests
proxies = {
    "http":"http://42.245.252.35:80"
}
url = "http://www.baidu.com"
r = requests.get(url,proxies=proxies)
print(r.status_code)
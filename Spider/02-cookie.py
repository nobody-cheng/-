import requests

url = "http://www.baidu.com"
proxies = {
    "http": "http://12.34.56.79:9527",
    "https": "http://12.34.56.79:9527",
}

req = requests.get(url)
# 返回cookie对象
cookie = req.cookies

# 将cookie对象转为字典
cookie_dict = requests.utils.dict_from_cookiejar(cookie)
# print(req.text)

print(cookie)

print(cookie_dict)
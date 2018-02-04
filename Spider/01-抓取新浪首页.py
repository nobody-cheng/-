"""
http://www.sina.com.cn/
"""
import requests
url= "http://www.sina.com.cn/"
req = requests.get(url)
print(req.text)

# print(req.content.decode())

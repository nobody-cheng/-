# coding=utf-8
import requests

img_url = "https://www.baidu.com/img/bd_logo1.png"

r = requests.get(img_url)  #发送请求
with open("baidu.png","wb") as f:
    f.write(r.content) #写入二进制数据
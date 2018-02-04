import requests

url = "http://www.renren.com/PLogin.do"
# 创建session对象,用来保存cookie
sess = requests.session()
# 处理headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "54.0.2840.99 Safari/537.36"
}

# 用户名及密码
data = {
    "email": "mr_mao_hacker@163.com",
    "password": "alarmchime"
}

# 发送附带用户名及密码的请求,登陆获取cookie,保存在session中
sess.post(url, data=data)

# sess包含了登陆后的cookie,可直接访问登陆后才能访问的页面
response = sess.get("http://share.renren.com/share/hot/v7")

print(response.text)

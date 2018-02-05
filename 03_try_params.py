# coding=utf-8
import requests

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}

# params = {"wd":"传智播客"}
# url_temp = "https://www.baidu.com/s"
#
# r = requests.get(url_temp,params=params,headers=headers)
# print(r.status_code)  #获取状态码
# print(r.request.url) #获取请求的url地址

# user_input = input("请输入搜索的关键字：")
# url = "https://www.baidu.com/s?wd={}".format(user_input)
# r = requests.get(url,headers=headers)
# print(r.status_code)
# print(r.request.url)

#TODO url解码
url_temp = "https%3a%2f%2fwww.baidu.com%2fs%3fie%3dutf-8%26f%3d8%26rsv_bp%3d1%26rsv_idx%3d1%26tn%3dbaidu%26wd%3durl%e8%a7%a3%e7%a0%81"
url_ret = requests.utils.unquote(url_temp)
print(url_ret)
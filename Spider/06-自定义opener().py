import urllib.request

# 构建一个HTTPHandler处理器对象,支持处理HTTP请求, 开启Debug Log，debuglevel 值默认 0
http_handler = urllib.request.HTTPHandler(debuglevel=1)
# # 构建一个HTTPSHandler处理器对象,支持处理HTTP请求
# https_handler = urllib.request.HTTPSHandler()

# 调用urllib.request.build_opener()方法,创建支持处理HTTP请求的opener对象
opener = urllib.request.build_opener(http_handler)

# 构建Request请求
request = urllib.request.Request("http://www.baidu.com/")

# 调用自定义opener对象的open()方法,发送request请求
response = opener.open(request)

# 获取服务器响应
print(response.read().decode())

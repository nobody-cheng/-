import urllib.request
import urllib.parse
"""
post 表单提交key=value
"""

url = "http://fanyi.youdao.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
}

formdata = {
    "type": "AUTO",
    "i": "i love python",
    "doctype": "json",
    "xmlVersion": "1.8",
    "keyfrom": "fanyi.web",
    "ue": "UTF-8",
    "action": "FY_BY_ENTER",
    "typoResult": "true"
}

data = urllib.parse.urlencode(formdata).encode()
print(data)
req = urllib.request.Request(url, data=data, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode())

# coding=utf-8
import requests
import json
import re

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
}
html_str = requests.get("http://36kr.com/",headers=headers).content.decode()

t = re.findall("<script>var props=(.*?),locationnal=",html_str)[0]
with open("36kr.json","w",encoding="utf-8") as f:
    f.write(t)
ret = json.loads(t)
print(ret)


import urllib.request
import ssl

context = ssl._create_unverified_context()

url = "https://www.12306.cn/mormhweb/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

req = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(req, context=context)
txt = response.read().decode()
print(txt)
with open("12306.html", "w") as f:
    f.write("hello")
    f.write(txt)

    f.close()

# coding=utf-8
from retrying import retry
import requests

@retry(stop_max_attempt_number=5)
def _parse_url(url):
    print("*"*100)
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
    response = requests.get(url,headers=headers,timeout=5)
    assert response.status_code == 200  #断言，状态码是200的时候，继续执行，否则会报错
    return response.content.decode()

def parse_url(url):
    try:
        response = _parse_url(url)
    except:
        response = ""
    return response

if __name__ == '__main__':
    url = "www.baidu.com"
    response = parse_url(url)
    print(response[:100])

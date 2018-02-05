# coding=utf-8
import requests
import re

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
}

cookie="anonymid=javrye2p-k1gxxq; depovince=GW; _r01_=1; JSESSIONID=abcG5HfLd-QsY-Rg7EUaw; _c1=0; jebecookies=9c1b2f9f-55c4-4549-8001-62a0f16ca30e|||||; ick_login=05fdf831-d02f-4fdf-a8fa-1e8cb6e805a1; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=8bd501b0f98e94b762de9ca0a86290159; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20171114/2045/main_Z50W_50a20000877d195a.jpg; t=8ae381a2b900feda20a0805b1687f6b79; societyguester=8ae381a2b900feda20a0805b1687f6b79; id=327550029; xnsid=d15058be; loginfrom=syshome; ch_id=10016; jebe_key=3cadae46-343b-4f95-8243-4aec1093b88b%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1512611759126%7C1%7C1512611759057; wp_fold=0"
cookies = {i.split("=")[0]:i.split("=")[-1] for i in cookie.split("; ")}
print(cookies)

url = "http://www.renren.com/327550029/profile"
response = requests.get(url,headers=headers,cookies=cookies)

print(re.findall("你瞅啥",response.content.decode()))
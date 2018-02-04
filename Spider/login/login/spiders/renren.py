# -*- coding: utf-8 -*-
import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/327550029/profile']

    def start_requests(self):
        # start_request 发送start_urls地址中的url请求
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
        }
        Cookie = "anonymid=j3jxk555-nrn0wh; _r01_=1; _ga=GA1.2.1274811859.1497951251; depovince=GW; jebecookies=b7f3745d-cbf3-45c7-bf71-2cb96af2ead9|||||; JSESSIONID=abcfqcIQSMiMJgM9MMNbw; ick_login=21f1f837-c416-4f8f-ae9d-25c14e46bf1c; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=503e316f6c0b733552952070082140279; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20171217/2145/main_mJgh_b0450000a72e195a.jpg; t=6807c5f2b3401a7523b041a16682291e9; societyguester=6807c5f2b3401a7523b041a16682291e9; id=327550029; xnsid=98655579; loginfrom=syshome; ch_id=10016; wp_fold=0"
        cookie_dict = {i.split('=')[0]: i.split('=')[-1] for i in Cookie.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            headers=headers,
            cookies=cookie_dict
        )

    def parse(self, response):
        with open("renren.html", 'w') as f:
            f.write(response.body.decode())
        yield scrapy.Request(
            "http://www.renren.com/327550029/profile?v=info_timeline",
            callback=self.parse_detail
        )

    def parse_detail(self, response):
        print(re.findall("毛兆军", response.body.decode()))

# -*- coding: utf-8 -*-
import scrapy
import re


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']
    print('====================================')

    def parse(self, response):
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        form_data = {
            "commit": "Sign in",
            "utf8": "✓",
            "authenticity_token": authenticity_token,
            "login": "noobpythoner",
            "password": "zhoudawei123"
        }
        yield scrapy.FormRequest(  # 发送post请求
            "https://github.com/session",
            formdata=form_data,
            callback=self.after_login
        )

    def after_login(self, response):
        print('***********************************', re.findall("noobpythoner|NoobPythoner", response.body.decode()))

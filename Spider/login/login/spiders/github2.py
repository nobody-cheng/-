# -*- coding: utf-8 -*-
import scrapy
import re


class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata={
                "login": "noobpythoner",
                "password": "zhoudawei123"
            },
            callback=self.after_login
        )

    def after_login(self, response):
        print('***********************************', re.findall("noobpythoner", response.body.decode()))

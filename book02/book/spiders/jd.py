# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import json

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com',"p.3.cn"]
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath("//div[@class='mc']/dl/dt")
        for dt in dt_list:
            item = {}
            item["b_cate"] = dt.xpath("./a/text()").extract_first()
            em_list = dt.xpath("./following-sibling::*[1]/em")
            for em in em_list[:1]:
                item["s_cate"] = em.xpath("./a/text()").extract_first()
                item["s_href"] = em.xpath("./a/@href").extract_first()
                if item["s_href"] is not None:
                    item["s_href"] = "https:"+item["s_href"]
                    yield  scrapy.Request(
                        item["s_href"],
                        callback=self.parse_book_list,
                        meta = {"item":deepcopy(item)}
                    )

    def parse_book_list(self,response):
        item = response.meta["item"]
        li_list = response.xpath("//ul[@class='gl-warp clearfix']/li")
        for li in li_list[:1]:
            item["book_img"] = li.xpath(".//div[@class='p-img']//img/@src").extract_first()
            item["book_img"] = "https:"+item["book_img"] if item["book_img"] is not None else None
            item["book_name"] = li.xpath(".//div[@class='p-name']//em/text()").extract_first().strip()
            item["book_author"] = li.xpath(".//span[@class='p-bi-name']/span/a/@title").extract()
            item["book_sku"] = li.xpath("./div/@data-sku").extract_first()
            #获取价格
            if item["book_sku"] is not None:
                price_url_tmep = "https://p.3.cn/prices/get?type=1&area=1_72_4137&ext=11000000&pin=&pdtk=&pduid=1513654671518371618242&pdpin=&pdbp=0&skuid=J_{}"
                yield scrapy.Request(
                    price_url_tmep.format(item["book_sku"]),
                    callback=self.parse_book_price,
                    meta={"item":deepcopy(item)}
                )

        #翻页
        next_url = response.xpath("//a[@class='pn-next']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                "https://list.jd.com" + next_url,
                callback=self.parse_book_list,
                meta = {"item":item}
            )

    def parse_book_price(self,response):
        '''[{"op":"23.40","m":"36.00","id":"J_11338771","p":"23.40"}]'''
        item = response.meta["item"]
        dict_response = json.loads(response.body.decode())
        item["book_price"] = dict_response[0]["op"]
        print(item,"*"*100)
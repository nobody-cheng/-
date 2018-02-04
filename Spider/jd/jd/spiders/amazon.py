# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    # start_urls = ['https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=sa_menu_top_books_l1?ie=UTF8&node=658390051']
    redis_key = 'amazon'
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='categoryRefinementsSection']/ul/li"),
             callback="parse_book_list", follow=True),
    )

    def parse_book_list(self, response):
        li_list = response.xpath("//div[@id='mainResults']/ul/li")
        for li in li_list:
            item = {}
            item['title'] = li.xpath(".//h2/text()").extract_first()
            item['img'] = li.xpath(".//img[@class='s-access-image cfMarker']/@src").extract_first()
            item['price'] = li.xpath(
                ".//div[@class='a-column a-span7']/div[@class='a-row a-spacing-none'][2]//span[@class='a-size-base a-color-price s-price a-text-bold']/text()").extract_first()
            item['author'] = li.xpath(".//div[@class='a-row a-spacing-small']/div[2]/span/text()").extract_first()
            item['num'] = li.xpath(".//div[@class='a-column a-span5 a-span-last']/div/a/text()").extract_first()
            item['url'] = li.xpath(".//h2/../@href").extract_first()
            if item['url'] is not None:
                print(item)
                yield scrapy.Request(
                    item['url'],
                    callback=self.parse_book_detail,
                    meta={"item": item}
                )

    def parse_book_detail(self, response):
        item = response.meta['item']
        pass

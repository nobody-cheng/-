import scrapy
from jd.items import JdItem
import json

i = 1
k = 1


class ComputerSpider(scrapy.Spider):
    name = 'computer'
    allowed_domains = ['jd.com', "p.3.cn", 'club.jd.com']
    start_urls = ['https://list.jd.com/list.html?cat=670%2C671%2C672']

    def parse(self, response):

        # response.xpath("//ul[@class='gl-warp clearfix']/li")
        li_list = response.xpath("//ul[@class='gl-warp clearfix']/li")

        for li in li_list:
            global k
            print('**********************第{}台********************'.format(k))
            k += 1
            item = JdItem()
            item['b_class'] = 'https:' + li.xpath(".//div[@class='p-img']/a/@href").extract_first() if len(
                li.xpath(".//div[@class='p-img']/a/@href")) > 0 else None
            item['type'] = li.xpath(".//div[@class='p-name']//em/text()").extract_first().split()
            item['num'] = li.xpath(".//a[@class='comment']/text()").extract_first()
            item['sku'] = li.xpath(".//div[@class='gl-i-wrap j-sku-item']/@data-sku").extract()

            # 获取评价数量和价格
            if item["sku"] is not None:
                print(item["sku"])
                if item["sku"] == []:
                    item['sku'] = li.xpath(
                        ".//div[@class='tab-content-item tab-cnt-i-selected j-sku-item']/@data-sku").extract()
                    yield scrapy.Request(
                        url='https://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds={}'.format(
                            item['sku'][0]),
                        callback=self.get_pingjia_num,
                        meta={'item': item}
                    )

                yield scrapy.Request(
                    url='https://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds={}'.format(
                        item['sku'][0]),
                    callback=self.get_pingjia_num,
                    meta={'item': item}
                )
        # 下一页
        next_url = response.xpath("//a[@class='pn-next']/@href").extract_first()
        if next_url is not None:
            global i
            print("+++++++++++++++++++++++++第{}页++++++++++++++++++++++++++".format(i))
            print("https://list.jd.com" + next_url)
            i += 1
            yield scrapy.Request(
                "https://list.jd.com" + next_url,
                callback=self.parse,
            )

    def get_pingjia_num(self, response):

        item = response.meta['item']
        dict_response = json.loads(response.body.decode(encoding="gbk"))['CommentsCount'][0]
        """{"CommentsCount": [{"SkuId": 4752553, "ProductId": 4752553, "ShowCount": 2200, "ShowCountStr": "2200+",
                            "CommentCountStr": "2.2万+", "CommentCount": 22000, "AverageScore": 5,
                            "DefaultGoodCountStr": "1.4万+", "DefaultGoodCount": 14000, "GoodCountStr": "2.1万+",
                            "GoodCount": 21000, "AfterCount": 200, "OneYear": 0, "AfterCountStr": "200+",
                            "GoodRate": 0.985, "GoodRateShow": 98, "GoodRateStyle": 148, "GeneralCountStr": "100+",
                            "GeneralCount": 100, "GeneralRate": 0.0080, "GeneralRateShow": 1, "GeneralRateStyle": 1,
                            "PoorCountStr": "100+", "PoorCount": 100, "PoorRate": 0.0070, "PoorRateShow": 1,
                            "PoorRateStyle": 1}]}"""

        item['num'] = dict_response['ShowCount']
        yield scrapy.Request(
            url='https://p.3.cn/prices/mgets?ext=11000000&pin=&type=1&area=1_72_4137_0&skuIds=J_{}&pdbp=0&pdtk=&pdpin=&pduid=1513685648145746696559'.format(
                item['sku'][0]),
            callback=self.parse_computer_price,
            meta={'item': item}
        )

    def parse_computer_price(self, response):

        item = response.meta['item']
        """[{"op":"6988.00","m":"9888.00","id":"J_5225346","p":"6699.00"}]"""
        try:
            dict_response = json.loads(response.body.decode(encoding="gbk"))[0]
        except Exception as e:
            dict_response = None
            item['price'] = '未找到价格'
            print(e)
        item['price'] = dict_response['p']
        yield item

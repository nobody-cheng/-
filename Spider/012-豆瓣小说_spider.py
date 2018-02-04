import requests
import json
import time


class DoubanSpider():
    def __init__(self):
        self.url_temp_list = [
            # {
            #     "url": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_book_fiction_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=0&_=1512809785581",
            #     "country": "小说"},
            {
                "url": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_book_detective_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=0&_=1512810090850",
                "country": "推理"
            }
        ]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3"
                          "202.94 Safari"
        }
        with open("豆瓣图书.csv", "a", encoding="gbk") as f:
            f.write("类型,图书,作者,演员,评分人数,评分" + "\n")

    def parse_url(self, url):
        """请求地址,得到json数据"""
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, json_response):
        """提取json数据"""
        dict_response = json.loads(json_response)
        # 得到页面的电影信息字典类型
        movie_info = dict_response["subject_collection_items"]
        total = dict_response["total"]
        return movie_info, total

    def save_movie(self, movie_info_list, country):
        """保存数据"""
        with open("豆瓣图书.csv", "a", encoding="gbk") as f:
            for move in movie_info_list:
                move["country"] = country
                # 构造列表,一条信息为一个元素
                temp_list = [move["country"], move["title"], move["author"], move["info"],
                             move["rating"]["count"], move["rating"]["value"]]
                print(temp_list)
                temp_str = ",".join([str(i) for i in temp_list]) + "\n"
                # print(temp_str)
                f.write(temp_str)

    def run(self):
        for url_temp in self.url_temp_list:
            num = 0
            total = 100
            i = 0
            # time.sleep(2)
            while num < total + 18:
                i += 1
                print("第%s次请求" % i)
                # 1.得到url
                url = url_temp["url"].format(num)
                print(url)
                # 2.请求地址,得到json数据
                json_response = self.parse_url(url)
                # 3.提取数据
                movie_info_list, total = self.get_content_list(json_response)
                # 4.保存数据
                self.save_movie(movie_info_list, url_temp["country"])
                # 向下翻页,加18条数据
                num += 18


if __name__ == '__main__':
    douban = DoubanSpider()
    douban.run()

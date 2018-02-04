import requests
import json


class DoubanSpider():
    def __init__(self):
        self.url_temp_list = [
            {
                "url": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288",
                "country": "美剧"},
            {
                "url": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_domestic_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288",
                "country": "国产剧"
            },
            {
                "url": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_hongkong_hot/items?os=windows%207&for_mobile=1&callback=jsonp1&start=0&count=18&loc_id=10",
                "country": "港剧"
            }
        ]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3"
                          "202.94 Safari"
        }
        with open("豆瓣电视剧.csv", "a", encoding="gbk") as f:
            f.write("国家,电视剧,导演,演员,评分人数,评分" + "\n")

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
        with open("豆瓣电视剧.csv", "a", encoding="gbk") as f:
            for move in movie_info_list:
                move["country"] = country
                # 构造列表,一条信息为一个元素
                temp_list = [move["country"], move["title"], "/".join(move["actors"]), "/".join(move["directors"]),
                             move["rating"]["count"], move["rating"]["value"]]
                # print(temp_list)
                temp_str = ",".join([str(i) for i in temp_list]) + "\n"
                f.write(temp_str)

    def run(self):
        for url_temp in self.url_temp_list:
            num = 0
            total = 100
            i = 0
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

# coding=utf-8
import requests
import re
import json

class Neihan:
    def __init__(self):
        self.start_url = "http://neihanshequ.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Host":"neihanshequ.com",
            "Referer":"http://neihanshequ.com/",
        }
        self.session = requests.session()

    def parse_url(self, url):
        print(url)
        response = self.session.get(url, headers=self.headers)
        return response.content.decode()

    def get_first_page_content_list(self,html_str):
        # print(html_str)
        content_list = re.findall(r"<h1 class=\"title\">.*?<p>(.*?)</p>",html_str,re.S)
        max_time = re.findall(r"max_time: '(.*?)',",html_str,re.S)[0]
        return content_list,max_time

    def save_content_list(self,content_list):#

        with open("neihan.text","a") as f:
            for content in content_list:
                f.write(content+"\n")
            # print(content_list)
            f.write("*"*100)

    def get_content_list(self,json_response):
        dict_response = json.loads(json_response)
        data_list = dict_response["data"]["data"]
        content_list = [i["group"]["content"] for i in data_list]
        max_time = dict_response["data"]["max_time"]
        has_more = dict_response["data"]["has_more"]
        return content_list,max_time,has_more

    def run(self):#实现主要逻辑
        #1.start_url
        #2.发送请求，获取响应
        html_str = self.parse_url(self.start_url)
        #3.提取数据,提取max_time
        content_list,max_time = self.get_first_page_content_list(html_str)
        #4.保存
        self.save_content_list(content_list)

        has_more = True #有第二页数据
        while has_more:
            print("*"*100)
            print("*"*100)
            print("*"*100)
            #5.第二页的url
            next_url = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time={}".format(max_time)
            # 2.发送请求，获取响应
            json_response = self.parse_url(next_url)
            # 3.提取数据,提取max_time
            content_list,max_time,has_more = self.get_content_list(json_response)
            # 4.保存
            self.save_content_list(content_list)
            #下一页的url，循环

if __name__ == '__main__':
    neihan = Neihan()
    neihan.run()

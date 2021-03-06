# coding=utf-8
import requests
import json
import sys



class BaiduFanyi:
    def __init__(self):
        self.post_url = "http://fanyi.baidu.com/v2transapi"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}


    def parper_post_data(self): #准备post的数据
        # self.user_input = input("请输入要翻译的文字:")
        self.user_input = sys.argv[1]
        post_data = {
            "from":"zh",
            "to":"en",
            "query":self.user_input,
            "transtype":"translang",
            "simple_means_flag":"3"
        }
        return post_data

    def parse_url(self,url,data): #发送请求，获取响应
        response = requests.post(url,data=data,headers=self.headers)
        return response.content.decode()

    def get_result(self,html_str): #提取数据，打印出来
        dict_response = json.loads(html_str) #json转化为字典
        ret = dict_response["trans_result"]["data"][0]["dst"]
        print("{}的翻译结果是：{}".format(self.user_input,ret))

    def run(self):#实现主要逻辑
        #1.url,post_data
        post_data = self.parper_post_data()
        #2.发送请求，获取响应
        html_str = self.parse_url(self.post_url,post_data)
        #3.提取数据
        self.get_result(html_str)

if __name__ == '__main__':
    # print(sys.argv[1])
    fanyi = BaiduFanyi()
    fanyi.run()
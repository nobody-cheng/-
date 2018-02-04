import requests
import json


class BaiduFanyi():
    """百度翻译"""

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
        }
        self.post_url = "http://fanyi.baidu.com/v2transapi"

    def post_data(self):
        self.user_input = input("请输入需要翻译的语言:")
        from_str = self.lan_detect(self.user_input)
        to_str = "en" if from_str == "zh" else "zh"  # 如果from是zh,to就是en

        post_data = {
            "from": from_str,
            "to": to_str,
            "query": self.user_input,
            "transtype": "translang",
            "simple_means_flag": "3"
        }
        return post_data

    def parse_url(self, url, data):
        """发送请求"""
        resp = requests.post(url, data=data, headers=self.headers)
        return resp.content.decode()

    def get(self, html_str):
        """提取数据"""
        print("提取数据")
        dict_resp = json.loads(html_str)  # 将json转为字典
        print(type(dict_resp))
        ret = dict_resp["trans_result"]["data"][0]["dst"]
        print("翻译结果是:{}".format(ret))

    def lan_detect(self, query_string):
        """语言检测"""
        lan_detect_url = "http://fanyi.baidu.com/langdetect"
        post_data = {
            "query": query_string
        }
        response = self.parse_url(lan_detect_url, post_data)
        dict_response = json.loads(response)
        ret = dict_response["lan"]
        return ret

    def run(self):
        """主逻辑"""
        # 1. 获取url
        post_data = self.post_data()
        # 2. 请求地址,获取响应
        html_str = self.parse_url(self.post_url, post_data)
        # 3. 提取数据,保存
        self.get(html_str)


if __name__ == '__main__':
    fanyi = BaiduFanyi()
    fanyi.run()

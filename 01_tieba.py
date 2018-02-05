# coding=utf-8
import requests
from retrying import retry
from lxml import etree

class TiebaSpider:
    def __init__(self,tieba_name):
        self.start_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw={}".format(tieba_name)
        self.headers= {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
        self.part_url ="http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/"

    @retry(stop_max_attempt_number=3)
    def _parse_url(self,url):
        response = requests.get(url,headers=self.headers,timeout=5)
        return response.content

    def parse_url(self,url):  #发送请求，获取响应
        print(url)
        try:
            html_str = self._parse_url(url)
        except:
            html_str = None
        return html_str

    def get_content_list(self,html_str):#提取列表页的数据
        # with open("baidu.html","w") as f:
        #     f.write(html_str)
        html = etree.HTML(html_str)
        #分组
        # html.xpath("//body/div/div[@class='i']|//body/div/div[@class='i x']")
        div_list = html.xpath("//body/div/div[contains(@class,'i')]")
        content_list = []
        for div in div_list: #对每一次提取数据
            item = {}
            #提取标题
            item["title"]=div.xpath("./a/text()")[0] if len(div.xpath("./a/text()"))>0 else None
            #提取url地址
            item["href"] = self.part_url+div.xpath("./a/@href")[0] if len(div.xpath("./a/@href"))>0 else None
            #提取图片
            item["img_list"] = self.get_img_list(item["href"],[])
            #提取大图
            item["img_list"] = [requests.utils.unquote(i).split("&src=")[-1] for i in item["img_list"]]
            content_list.append(item)
        #提取下一页的url地址
        next_url = html.xpath("//a[text()='下一页']/@href")
        if len(next_url)>0:
            next_url = self.part_url+next_url[0]
        else:
            next_url = None

        return content_list,next_url

    def get_img_list(self,detail_url,total_img_list):#获取帖子中的所有的图片
        if detail_url is not None:
            # 4.请求帖子的地址
            detail_html_str = self.parse_url(detail_url)
            # 5.提取帖子详情页的图片地址，下一页的url地址
            detail_html = etree.HTML(detail_html_str)
            img_list = detail_html.xpath("//img[@class='BDE_Image']/@src")
            total_img_list += img_list
            detail_next_url = detail_html.xpath("//a[text()='下一页']/@href")  #获得下一页的url地址的一个列表
            #可以更具detail_next_url 长度是否为0 来判断是否有下一页
            # 6.请求下一页的URL地址，循环4-6步，详情页么有下一页结束
            if len(detail_next_url)>0:
                detail_next_url = self.part_url+detail_next_url[0]  #下一页的url
                return self.get_img_list(detail_next_url,total_img_list)
            else:
                return total_img_list
        else:
            return total_img_list

    def save_content_listr(self,content_list):
        for content in content_list:
            print(content)
        print("保存成功")

    def run(self):#实现主要逻辑
        next_url = self.start_url
        while next_url is not None:
            #1.start_url
            #2.获取第一页的列表页的页面内容
            html_str= self.parse_url(next_url)
            #3.从列表页提取数据，帖子地址，帖子标题，下一页的url地址
            # 4.请求帖子的地址
            # 5.提取帖子详情页的图片地址，下一页的url地址
            # 6.请求下一页的URL地址，循环4-6步，详情页么有下一页结束
            content_list,next_url  = self.get_content_list(html_str)
            self.save_content_listr(content_list)
            #7.请求列表页的下一页，进入循环2-7步，列表页没有下一页的时候结束



if __name__ == '__main__':
    tieba = TiebaSpider("中粮")
    tieba.run()

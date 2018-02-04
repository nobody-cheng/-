from selenium import webdriver
from retrying import retry
import time
class douyuSpider():
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@id='live-list-contentbox']/li")
        content_list = []
        for li in li_list:
            item = {}
            item['title'] = li.find_element_by_xpath("./a").get_attribute('title')
            item["watch_num"] = li.find_element_by_xpath(".//span[@class='dy-num fr']").text
            print(item)
        next_url = self.driver.find_element_by_xpath("//a[@class='shark-pager-next']")
        next_url = next_url[0] if len(next_url)>0 else None
        return content_list,next_url

    def save_content_list(self, content_list):
        print('保存成功')

    def run(self):
        self.driver.get(self.start_url)
        # 提取数据
        content_list, next_url = self.get_content_list()
        self.save_content_list(content_list)
        # 点击下一页，进入循环
        while next_url is not None:
            next_url.click()
            time.sleep(8)
            # 提取数据
            content_list, next_url = self.get_content_list()
            # 4.保存
            self.save_content_list(content_list)
if __name__ == '__main__':
    douyu = douyuSpider()
    douyu.run()
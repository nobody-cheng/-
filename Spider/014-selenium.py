from selenium import webdriver
import time

url = "https://www.baidu.com/"

# 实例化driver
driver = webdriver.Chrome()
# 请求网址
driver.get(url)
# 定位元素,输入内容
driver.find_element_by_id('kw').send_keys('习近平')
# 定位元素,点击搜索
driver.find_element_by_id('su').click()

print(driver.current_url)
time.sleep(10)
driver.quit()
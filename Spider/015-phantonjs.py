from selenium import webdriver
import time

url = "https://www.baidu.com/"
# 实例化对象
driver = webdriver.PhantomJS()
# 请求地址
driver.get(url)

# 默认保存窗口
# driver.save_screenshot('./img.png')

# 设置窗口大小
# driver.set_window_size(1920, 1080)
# driver.save_screenshot('./img2.png')

# 获取
# print(driver.page_source)

print(driver.get_cookies())

print('获取cookies====', {i["name"]: i["value"] for i in driver.get_cookies()})
driver.save_screenshot('./img3.png')

time.sleep(10)
driver.quit()

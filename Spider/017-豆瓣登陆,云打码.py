from selenium import webdriver
import time
from yundama.dama import indetify

import requests

url = 'https://www.douban.com/'
driver = webdriver.Chrome()
driver.get(url)

# 获取输入框,输入账号
driver.find_element_by_id('form_email').send_keys("784542623@qq.com")
# 获取输入框,输入密码
driver.find_element_by_id('form_password').send_keys('zhoudawei123')

time.sleep(6)

# 获取验证码的地址
captcha_url = driver.find_element_by_id("captcha_image").get_attribute('src')
# 获取图片的bytes字节数
response = requests.get(captcha_url)
ret = indetify(response.content)
print('验证码识别==', ret)

# 输入验证码
driver.find_element_by_id('captcha_field').send_keys(ret)

# 点击登陆/
driver.find_element_by_class_name('bn-submit').click()

time.sleep(6)

cookies_list = driver.get_cookies()
cookie_dict = {i['name']: i['value'] for i in cookies_list}
print(cookie_dict)
time.sleep(10)
driver.quit()

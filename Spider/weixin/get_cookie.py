from selenium import webdriver
import time
import json

user = '13823875990@139.com'
pwd = '1zhangcheng'
login_url = 'https://mp.weixin.qq.com/'

# 登陆,获取登陆后的cookies信息,并保存到本地

cookie_dict = {}
print('启动浏览器,打开登陆界面')
driver = webdriver.Chrome()
driver.get(login_url)
time.sleep(5)
print('正在输入账号和密码.....')
# 清空账号输入框
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/form/div[1]/div[1]/div/span/input').clear()
# 输入账号
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/form/div[1]/div[1]/div/span/input').send_keys(
    user)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/form/div[1]/div[2]/div/span/input').clear()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/form/div[1]/div[2]/div/span/input').send_keys(
    pwd)
# 记住账号
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/form/div[3]/label/i').click()
# 点击登陆
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/form/div[4]/a').click()
time.sleep(10)  # 方便手机扫描

cookie_items = driver.get_cookies()
for item in cookie_items:
    cookie_dict[item['name']] = item['value']
# 将cookies转成json形式并存入本地名为cookie的文本中
cookie_str = json.dumps(cookie_dict)
with open('./cookie.txt', 'w+', encoding='utf-8') as f:
    f.write(cookie_str)
time.sleep(10)
driver.close()
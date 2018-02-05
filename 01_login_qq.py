# coding=utf-8
from selenium import webdriver
import time
from pprint import pprint

driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")

#切换frame
driver.switch_to_frame("login_frame")
driver.switch_to.frame("login_frame")

driver.find_element_by_id("u").send_keys("1111111")

time.sleep(5)
driver.quit()

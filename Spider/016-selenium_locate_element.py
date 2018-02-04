from selenium import webdriver
import time
url = 'http://36kr.com/'

driver = webdriver.Chrome()
driver.get(url)

# find_element 返回的是一个元素对象,如果无,则报错
t1 = driver.find_element_by_class_name('feed_ul')
print('t1====', t1)

# find_elements 返回一个列表,如果无,则返回空列表
t2 = driver.find_elements_by_class_name('feed_ul')
print('t2====', t2)


ul_list = driver.find_elements_by_xpath(".//ul[@class='feed_ul']/li")

for ul in ul_list:
    print(ul)
    title = ul.find_element_by_xpath("//div[@class='img_box']//img").get_attribute('alt')
    print(title)
"""已经取到了所有的li标签,get都是同一个标题内容"""

time.sleep(90)
driver.quit()
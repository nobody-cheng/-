# coding=utf-8
from lxml import etree

text = ''' <div> <ul> 
        <li class="item-1"><a>first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a>
        </ul> </div> '''
#etree.HTML()能够处理str和bytes的数据
html = etree.HTML(text)
print(html)

#etree.tostring element转化为字符串
# t1 = etree.tostring(html).decode()
# print(t1)

#item-1 的li下的a的href
temp1 = html.xpath("//li[@class='item-1']/a/@href")
print(temp1)

#item-1 的li下的a的文本
temp2 = html.xpath("//li[@class='item-1']/a/text()")
print(temp2)

print("*"*20)
#假设每个li标签是一条新闻，href是url地址，文本是标题，要组成一个字典
for href in temp1:
    item = {}
    item["href"] = href
    item["title"] = temp2[temp1.index(href)]
    print(item)

temp3 = html.xpath("//li[@class='item-1']")  #分组
print(temp3)
print("*"*100)
for li in temp3: #取每一个li标签里面的内容
    item = {}
    item["href"] = li.xpath("./a/@href")[0] if len(li.xpath("./a/@href"))>0 else None
    item["title"] = li.xpath("./a/text()")[0] if len(li.xpath("./a/text()"))>0 else None
    print(item)
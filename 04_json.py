# coding=utf-8
import json
import requests
url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288"

json_response = requests.get(url).content.decode()

#json.loads
t1 = json.loads(json_response)  #把json字符串转化为字典
# print(t1)
# print(type(t1))

#json.dumps
# t2 = json.dumps(t1)  #把字典转化为json字符串
# print(t2)
# print(type(t2))

# with open("douban.txt","w") as f:
#     #ensure_ascii 保存中文还是中文
#     #indent 换行和空格
#     t2 = json.dumps(t1,ensure_ascii=False,indent=2)
#     f.write(t2)

#json.load()  #实现含有json的类文件对象和python类型的转化
with open("douban.txt","r") as f:
    # t3 = json.load(f)
    t3 = json.loads(f.read())
# print(t3)
# print(type(t3))

#json.dump() #实现python类型和类文件对象的转化
with open("douban.text","w") as f:
    json.dump(t3,f,ensure_ascii=False,indent=4)



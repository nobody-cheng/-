# coding=utf-8
from pymongo import MongoClient

client = MongoClient(host="localhost",port=27017)
collection = client["test100"]["t1"]

#插入数据
# ret1 = collection.insert_one({"_id":"10003","name":"jack","age":20})
# print(dir(ret1))
# print(ret1.inserted_id)

#插入多条数据
# data_list = [
#     {"name":"a","age":13},
#     {"name": "b", "age": 14},
# ]
# collection.insert_many(data_list)

# 查找多个结果
# ret= collection.find({"name":"jack"})  #结果是一个游标类型，类似文件指针
# print(ret)
# for i in ret:
#     print(i)
# print("*"*100)
# for i in ret:
# #     print(i)
# ret_list = list(ret)
# ret_list2 = list(ret)
# print(ret_list,ret_list2)

#查找一个结果
# print(collection.find_one({"name":"jack"}))

#跟新一条数据
# collection.update_one({"name":"jack"},{"$set":{"age":1000}})
#跟新多条数据

collection.update_many({"name":"jack"},{"$set":{"age":1000}})

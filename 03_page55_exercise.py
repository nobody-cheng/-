# coding=utf-8
from pymongo import MongoClient
data_list = [{"_id":i,"name":"py{}".format(i)} for i in range(0,1000)]

client = MongoClient(host="localhost",port=27017)
collection = client["t251"]["t1"]
#问题1
# collection.insert_many(data_list)

#问题2
ret = collection.find()
t = [i["name"] for i in ret if i["_id"]%100==0]
print(t)
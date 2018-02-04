from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)
collection = client["test100"]['t1']

# 插入数据
# ret = collection.insert_one({'_id': '1001', 'name': '习近平', 'age': '66'})


# 插入多条数据
# data_list = [
#     {'name': 'a', "age": "10"},
#     {'name': 'b', 'age': 88}
# ]
# collection.insert_many(data_list)


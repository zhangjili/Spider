# coding=utf-8
from pymongo import MongoClient

# 实例化client，建立连接
client = MongoClient(host="192.168.216.132", port=27017)
collection = client["test"]["t251"]

# 插入一条数据
# ret1 = collection.insert_one({"_id": 100, "name": "xiaowang", "age": 10})
# print(ret1)

# 插入多条数据
# data_list = [{"name":"test{}".format(i)} for i in range(10)]
# collection.insert_many(data_list)

# 查询一个记录
# t = collection.find_one({"name":"xiaowang"})
# print(t)
# 查询所有记录
t = collection.find({"name": "xiaowang"})
print(t)

# for i in t:
#     print(i)
# #
# for j in t:
#     print(j,"*"*100)
# 强制转换,把字典放在list中
print(list(t))

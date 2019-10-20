# coding=utf-8
from pymongo import MongoClient

client = MongoClient(host="192.168.216.132", port=27017)
collection = client["test"]["t252"]

# data_list = [ {"_id":i,"name":"py{}".format(i)} for i in range(10)]
# collection.insert_many(data_list)

ret = collection.find()
data_list = list(ret)
data_list = [i for i in data_list if i["_id"] % 2 == 0 and i["_id"]!=0]
print(data_list)
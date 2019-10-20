# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    #  process_item名字也不能改,只能这样写,因为父类中有这个方法,必须继续写这个方法
    def process_item(self, item, spider):
        #TODO
        item["hello"] = "world"
        # print(item)
        return item # 如果不return,得到的将是none值

class MyspiderPipeline1(object):
    def process_item(self, item, spider):
        print(item)
        return item
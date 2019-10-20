# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
# JsonLinesItemExporter 一行一行的写
from scrapy.exporters import JsonItemExporter,JsonLinesItemExporter


# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open("duanzi.json",'w',encoding="utf-8")
#
#     # 爬虫打开的时候回调用这个函数
#     def open_spider(self, spider):
#         print('爬虫开始了')
#
#     # 爬虫运行过程中会调用这个函数 , spiders yield 的数据会传到item中
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item),ensure_ascii=False)
#         self.fp.write(item_json+'\n')
#         return item
#
#     # 爬虫结束的时候回调用这个函数
#     def close_spider(self, spider):
#         self.fp.close()
#         print('爬虫结束了')
# 第二种方式写入 如果数据量比比较大的时候很耗内存
# class QsbkPipeline(object):
#     def __init__(self):
#         # JsonItemExporter 是以二进制的形式打开和写入的,所以要加b
#         self.fp = open("duanzi.json", 'wb')
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#         self.exporter.start_exporting()
#
#     # 爬虫打开的时候回调用这个函数
#     def open_spider(self, spider):
#         print('爬虫开始了')
#
#     # 爬虫运行过程中会调用这个函数 , spiders yield 的数据会传到item中
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     # 爬虫结束的时候回调用这个函数
#      def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print('爬虫结束了')
            # 第三种方式写入 数据量多的时候可以这么写,每次处理数据的时候就直接存储到硬盘中
class QsbkPipeline(object):
    def __init__(self):
        # JsonItemExporter 是以二进制的形式打开和写入的,所以要加b
        self.fp = open("duanzi.json", 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
    # 爬虫打开的时候回调用这个函数
    def open_spider(self, spider):
        print('爬虫开始了')
    
    # 爬虫运行过程中会调用这个函数 , spiders yield 的数据会传到item中
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
    # 爬虫结束的时候回调用这个函数
    def close_spider(self, spider):
        self.fp.close()
        print('爬虫结束了')

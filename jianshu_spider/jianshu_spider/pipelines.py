# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# 专门用来做数据库处理的 数据库连接池
from twisted.enterprise import adbapi
from pymysql import cursors

# 第一种方式 同步式
class JianshuSpiderPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'jianshu',
            'charset': 'utf8'
        }
        self.conn = pymysql.Connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None
    
    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['title'], item['content'], item['pub_time'],item['origin_rul']))
        self.conn.commit()
        return item
    
    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into article(id,title,content,pub_time,origin_rul) values(null,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql
    
    
    
    
    
# 第二种方式  异步方式
class JianshuTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'jianshu',
            'charset': 'utf8',
            'cursorclass':cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql',**dbparams)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
               insert into article(id,title,content,pub_time,origin_rul,read_count,word_count,subjects) values(null,%s,%s,%s,%s,%s,%s,%s)
               """
            return self._sql
        return self._sql

    def process_item(self,item, spider):
         defer = self.dbpool.runInteraction(self.insert_item,item)
         defer.addErrback(self.handle_error,item,spider)
    
    def insert_item(self,cursor,item):
        cursor.execute(self.sql,(item['title'], item['content'], item['pub_time'],item['origin_rul'],item['read_count'],item ['word_count'],item['subjects']))
   
    def handle_error(self,error,item,spider):
        print('='*10+"error"+'=='*10)
        print(error)
        print('=' * 10 + "error" + '==' * 10)
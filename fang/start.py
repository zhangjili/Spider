# encoding: utf-8
from scrapy import cmdline
# 启动爬虫
# cmdline.execute(['scrapy','crawl','wxapp_spider'])
# 或者
cmdline.execute("scrapy crawl sfw".split())
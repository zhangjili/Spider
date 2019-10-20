# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 爬虫名
    allowed_domains = ['itcast.cn']  # 允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  # 最开始请求的url地址

    # 方法名必须是parse,因为父类中有这个方法,但是没有写完,所以必须继续写这个方法
    def parse (self, response):
        # 处理start_url地址对应的响应 extract()去除掉xpath
        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret1)

        # 分组
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = {}
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            # print(item)
            # Request, BaseItem, dict or None
            # yield item 把item字典传递给pipelines.py, yield 减少内存占用率 yield 列表无效,不能这样做 ,
            # 只能yield Request, BaseItem, dict or None
            yield item

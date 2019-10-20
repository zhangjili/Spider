# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['lovehhy.net']
    start_urls = ['http://www.lovehhy.net/Joke/Detail/QSBK/1']
    base_domain = 'http://www.lovehhy.net'

    def parse(self, response):
        # # response 的类型是<class 'scrapy.http.response.html.HtmlResponse'>
        # print("#"*30)
        # print(type(response))
        # print("#"*30)
        # h3_all content_all 的类型是<class 'scrapy.selector.unified.SelectorList'>是一个列表
        h3_all = response.xpath("//div[@id='footzoon']//h3")
        content_all = response.xpath("//div[@id='footzoon']//div[@id='endtext']")
        # print("#"*30)
        # print(type(contentLeft))
        # print("#"*30)
        # duanzidiv 的类型是 Selector类型
        a = []
        for duanzidiv in h3_all:
            title = duanzidiv.xpath("./a/text()").get().strip()
            a.append(title)
            # print(a)
        b = []
        for content1 in content_all:
            # getall() 获取的是所有的文本
            content = content1.xpath("./text()").getall()
            # 把列表里的内容变成字符串
            content = "".join(content).strip()
            b.append(content)
            # print(b)
        # duanzis = []
        for value in zip(a,b):
            title,content = value
            # duanzi = {
            #     'title':title,
            #     'content':content
            # }
            item = QsbkItem(title=title,content=content)
            # duanzis.append(duanzi)
            # 把字典移交给pipeline

            # print(item)

            yield item
        # print(duanzis)
        next_url = response.xpath("//div[@id='ct_page']/ul/li[last()]/a/@href").get()
        print(self.base_domain+next_url)
        yield scrapy.Request(self.base_domain+next_url,callback=self.parse)
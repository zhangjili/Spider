# -*- coding: utf-8 -*-
from jianshu_spider.items import ArticleItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com']
    
    rules = (
        # href="/p/727e47f2a62c" .+ .* 或者不写都可以
        Rule(LinkExtractor(allow=r'.+/p/[0-9a-z]{12}'), callback='parse_detail', follow=True),
    )
    
    def parse_detail(self, response):
        title = response.xpath("//h1[@class='_1RuRku']/text()").get()
        pub_time = response.xpath("//div[@class='s-dsoj']//time/text()").get()
        word_count = response.xpath("//div[@class='s-dsoj']/span/text()")[0].get()
        read_count = response.xpath("//div[@class='s-dsoj']/span/text()")[1].get()
        # 把HTML格式也拿了出来 get()只会得到纯文本
        content = response.xpath("//div[@class='_gp-ck']").get()
        subjects = "".join(response.xpath("//div[@class='_2Nttfz']/a/span/text()").getall())
        
        item = ArticleItem(
            title=title,
            pub_time=pub_time,
            origin_rul=response.url,
            content=content,
            word_count=word_count,
            read_count=read_count,
            subjects=subjects
        
        )
        yield item

# -*- coding: utf-8 -*-

import scrapy
from bmw.items import BmwItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class Bmw5Spider(CrawlSpider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html#pvareaid=3454438']
    
    rules = (
        Rule(
            LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/65.+'),
            callback="parse_page",
            follow=True
        ),
    )

    def parse_page(self, response):
        category = response.xpath("//div[@class='uibox']/div/text()").get()
        print(category)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        srcs = response.xpath("//div[contains(@class,'uibox-con')]/ul/li//img/@src").getall()
        # 把map转化为列表,把小图的url变成大图的url,再加上前缀
        srcs = list(map(lambda url: response.urljoin(url.replace("240x180_0_q95_c42","1024x0_1_q95")), srcs))
        # map(lambda url:response.urljoin(url),srcs)
        # for i in srcs:
        #     print(i)
        yield BmwItem(category=category,image_urls=srcs)
        
    
    
    def test_parse(self,response):
        uiboxs = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxs:
            category = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            # 把map转化为列表,加上前缀
            urls = list(map(lambda url: response.urljoin(url.replace), urls))
            item = BmwItem(category=category, image_urls=urls)
            yield item
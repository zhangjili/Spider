# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from boss.items import BossItem


class ZhipingSpider(CrawlSpider):
    name = 'zhiping'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=python&page=1']
    
    rules = (
        # 匹配职位列表页的规则 https://www.zhipin.com/c101010100/?query=python&page=1
        Rule(LinkExtractor(allow=r'(.+\?query=python&page=\d)'), follow=True),
        # 匹配职位详情页的规则
        Rule(LinkExtractor(allow=r'.+(job_detail.+\.html)'), callback="parse_job", follow=False)
    )
    # https://www.zhipin.com/job_detail/191c8cbe2b54156103R93t-5ElY~.html
    
    def parse_job(self, response):
        name = response.xpath("//h1[@class='name']/text()").get().strip()
        print(name)
        salary = response.xpath("//h1[@class='name']/span/text()").get().strip()
        job_info = response.xpath("//div[@class='job-primary']/div[@class='info-primary']/p//text()").getall()
        city = job_info[0]
        work_years = job_info[1]
        education = job_info[2]
        company = response.xpath("//div[@class='info-company']//a/text()").get()
        item = BossItem(
            name=name,
            salary=salary,
            city=city,
            work_years=work_years,
            education=education,
            company=company
        )
        print(item)
        return item

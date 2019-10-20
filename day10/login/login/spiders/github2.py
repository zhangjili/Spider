# -*- coding: utf-8 -*-
import scrapy
import re


class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response, #自动的从response中寻找from表单
            formdata={"login":"1036661407@qq.com","password":"18737807203zhang"},
            callback = self.after_login
        )

    def after_login(self,response):
        print(re.findall("zhangjili",response.body.decode()))


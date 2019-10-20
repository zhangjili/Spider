# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    # def parse(self, response):
    #     pass
    # 因为要登陆,所以要重写start_requests方法
    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        data = {
            "email":'18438622650',
            "password":"18737807203zhang"
        }
        request = scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield request
        
    def parse_page(self,reponse):
        request = scrapy.Request(url='http://www.renren.com/972239077/profile', callback=self.parse_profile)
        yield request
        
    def parse_profile(self,response):
        with open("db.html",'w',encoding="utf-8") as f:
            f.write(response.text)
    
    
    
    

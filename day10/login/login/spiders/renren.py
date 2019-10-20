# -*- coding: utf-8 -*-
import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/972239077/profile']

    def start_requests(self):
        cookies = "anonymid=k0hyz431-7bnj7b; _r01_=1; " \
                  "jebe_key=92a1837e-61df-4569-a719-deae45111647%7C553a534b8be4669a3c8d8683c978bc9a%7C15" \
                  "68370123116%7C1%7C1568370125260; ln_uact=18438622650; ln_hurl=http://head.xiaonei.com" \
                  "/photos/0/0/men_main.gif; _de=1C73EBEBE8D9EA55BB154F572C6DC035; depovince=BJ; jeb" \
                  "ecookies=260aa3ab-ff48-47e8-878c-a4b5716e21a7|||||; JSESSIONID=abcqzzPEfEPRld-1Pdk1w; ick_lo" \
                  "gin=abafd1d1-74fa-4bb4-9d79-83fb374f1735; p=51c6367124ba2425279216701a9389d17; first_login_flag" \
                  "=1; t=d9d6aeb71420cc2d48e919e651be8e037; societyguester=d9d6aeb71420cc2d48e919e651be8e037; " \
                  "id=972239077" \
                  "; xnsid=b5f11fb2; loginfrom=syshome; jebe_key=92a1837e-61df-4569-a" \
                  "719-deae45111647%7C553a534b8be4669a3c" \
                  "8d8683c978bc9a%7C1568370123116%7C1%7C1568905556125"
        # 把cookies 变成字典
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        # headers = {"Cookie":cookies}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
            # headers = headers
        )

    def parse(self, response):
        print(re.findall("黑子",response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/972239077/profile?v=info_timeline",
            callback=self.parse_detial
        )

    def parse_detial(self,response):
        print(re.findall("感情状态",response.body.decode()))

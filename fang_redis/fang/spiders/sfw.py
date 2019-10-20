# -*- coding: utf-8 -*-
import re

import scrapy
from fang.items import NewHouseItem,ESFHouseItem
from scrapy_redis.spiders import RedisSpider

class SfwSpider(RedisSpider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    # start_urls = ['https://www.fang.com/SoufunFamily.htm']
    # 从redis数据库中redis_key中读取url
    redis_key = "fang:start_urls"
    
    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        province = None
        for tr in trs:
            tds = tr.xpath(".//td[not(@class)]")
            province_td = tds[0]
            province_text = province_td.xpath(".//text()").get()
            province_text = re.sub(r'\s', "", province_text)
            if province_text:
                province = province_text
            if province == '其它':
                continue
            city_td = tds[1]
            city_links = city_td.xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                # print("省份",province)
                # print("城市",city)
                # print("城市链接",city_url)
                url_model = city_url.split(".", 1)
                print("**********"+url_model)
                scheme = url_model[0]
                domain = url_model[1]
                
                newhouse_url = scheme + ".newhouse." + domain + "house/s"
                esf_url = scheme + ".esf." + domain
                # print(newhouse_url, esf_url)
                
                # yield scrapy.Request(url=newhouse_url,
                #                      callback=self.parse_newhouse,
                #                      meta={"info": (province, city)})  # 元组
                yield scrapy.Request(url=esf_url,
                                     callback=self.parse_esf,
                                     meta={"info": (province, city)})  # 元组
                
            
    def parse_newhouse(self, response):
        province, city = response.meta.get("info")
        lis = response.xpath("//div[contains(@class,'nl_con')]//ul/li")
        for li in lis:
            name = li.xpath(".//div[@class='nlcd_name']/a/text()").get()
            if name is not None:
                name = name.strip()
                # print(name)
                house_type_list = li.xpath(".//div[contains(@class,'house_type ')]/a//text()").getall()
                house_type_list = list(map(lambda x:re.sub(r'\s',"",x),house_type_list))
                rooms = list(filter(lambda x:x.endswith('居'),house_type_list))
                area = "".join(li.xpath(".//div[contains(@class,'house_type')]/text()").getall())
                area = re.sub(r'\s|－|/'," ",area).strip()
                address = li.xpath(".//div[@class='address']/a/@title").get()
                district_text = "".join(li.xpath(".//div[@class='address']/a//text()").getall())
                district = re.search(r".*\[(.+)\].*",district_text).group(1)
                sale = li.xpath(".//div[contains(@class,'fangyuan')]/span/text()").get()
                price = "".join(li.xpath(".//div[@class='nhouse_price']//text()").getall())
                price = re.sub(r'\s|广告',"",price)
                origin_url = li.xpath(".//div[@class='nlcd_name']/a/@href").get()
                origin_url = "https:"+origin_url
                item =NewHouseItem(
                    name=name,
                    rooms=rooms,
                    areas=area,
                    address=address,
                    district=district,
                    sale=sale,
                    price=price,
                    origin_url=origin_url,
                    province=province,
                    city=city
                )
                yield item
        next_url = response.xpath("//div[@class='page']//a[@class='next']/@href").get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url),callback=self.parse_newhouse,meta={"info":(province,city)})
            # print(response.urljoin(next_url))
        

    def parse_esf(self, response):
        province, city = response.meta.get("info")
        dls = response.xpath("//div[contains(@class,'shop_list')]/dl")
        item=ESFHouseItem()
        for dl in dls:
            item = ESFHouseItem(province=province,city=city)
            name = dl.xpath(".//p[@class='add_shop']/a/text()").get()
            if name is not None:
                name = name.strip()
            item['name'] = name
            infos = dl.xpath(".//p[@class='tel_shop']/text()").getall()
            infos =list(map(lambda x:re.sub(r'\s',"",x),infos))
            for info in infos:
                if "厅" in info:
                    item['rooms'] = info
                elif '层' in info:
                    item['floor'] = info
                elif '向' in info:
                    item['toward'] = info
                elif '年' in info:
                    item['year'] = info.replace('年建',"")
                elif '㎡' in info:
                    item["area"] = info
                # print(item)
            address = dl.xpath(".//p[@class='add_shop']/span/text()").get()
            item['address'] = address
            item['price'] = "".join(dl.xpath(".//dd[@class='price_right']/span[1]//text()").getall())
            item['unit'] = "".join(dl.xpath(".//dd[@class='price_right']/span[2]//text()").getall())
            item['origin_url'] = response.urljoin((dl.xpath(".//h4[@class='clearfix']/a/@href").get()))
            # print(item['origin_url'])
            yield item
        next_url = response.xpath("//div[@class='page_al']/p[1]/a/@href").get()
        next_url = response.urljoin(next_url)
        yield scrapy.Request(url=next_url,callback=self.parse_esf,meta={'info':(province,city)})
            
        
        
        
        
        

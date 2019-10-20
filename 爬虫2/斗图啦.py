# -*- coding: gbk -*-
import requests
from lxml import etree
from urllib import request
import os
import re
def parse_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    print(imgs)
    for i in imgs:
        # print(etree.tostring(i))
        img_url = i.xpath(".//@data-original")[0]                            #或者是用  get('data-original') 为什么呢
        print(img_url)
        # print(img_url)
        alt = i.get('alt')
        alt = re.sub(r'[\??\.，。！!]','',alt)
        # suffix 得到的是元组,取第二个
        suffix = os.path.splitext(img_url)[1]
        filename = alt + suffix
        #print(suffix)
        print(filename)
        request.urlretrieve(img_url,'images/'+filename)
    
def main():
    for x in range(1,101):
        url = 'https://www.doutula.com/photo/list/?page={}'.format(x)
        parse_page(url)
        break


if __name__ == '__main__':
    main()
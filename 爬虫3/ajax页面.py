# coding=utf-8
import requests
from lxml import etree

def request_liet_page():
    url ='https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
    headers = {
         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36",
         'Referer':"https://www.lagou.com/jobs/list_python/p-city_2?&cl=false&fromSearch=true&labelWords=&suginput=",
         'Cookie':"user_trace_token=20191005142953-92a963fd-34a2-44ce-960e-23ad959bda5e; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570256992; _ga=GA1.2.578400505.1570256992; LGSID=20191005142953-8ab7542c-e739-11e9-a53a-5254005c3644; LGUID=20191005142953-8ab75664-e739-11e9-a53a-5254005c3644; sajssdk_2015_cross_new_user=1; _gid=GA1.2.1614472480.1570257015; gate_login_token=9ae944a3c0713b7c0a0dedf7bb0056749c9c76ff787209e1c6e2a7fef60026e3; LG_LOGIN_USER_ID=694ba190689fd250ae73e4aeb06f5658f40d66da56b8b62cdc797bad19c7b337; LG_HAS_LOGIN=1; _putrc=43F4E85C399E563B123F89F2B170EADC; JSESSIONID=ABAAABAAADEAAFIB40A0470A817A5B1644BB35278F1540F; login=true; unick=%E5%BC%A0%E5%90%89%E5%88%A9; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; privacyPolicyPopup=false; index_location_city=%E5%8C%97%E4%BA%AC; WEBTJ-ID=20191005143201-16d9a9e3016301-0dfd3b9e97964b-67e153a-2073600-16d9a9e3017803; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d9a9c90f9319-019e21e8ed18bd-67e153a-2073600-16d9a9c90fa655%22%2C%22%24device_id%22%3A%2216d9a9c90f9319-019e21e8ed18bd-67e153a-2073600-16d9a9c90fa655%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; TG-TRACK-CODE=search_code; X_HTTP_TOKEN=f81221e580b64ae894285207518164dbf8a21cbc1a; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570258247; LGRID=20191005145049-771fd601-e73c-11e9-97fa-525400f775ce; SEARCH_ID=042ccedea37c441a98503864b67a0783",
         'Origin':"https://www.lagou.com",
         'Host':"www.lagou.com",
         'Accept':"application/json, text/javascript, */*; q=0.01",
         'Accept-Encoding':"gzip, deflate, br",
         'Accept-Language':"zh-CN,zh;q=0.9",
         'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",
         'X-Anit-Forge-Code':"0",
         'X-Anit-Forge-Token':"None",
         'X-Requested-With':"XMLHttpRequest"
    }
    data = {
        'first':"false",
        'pn':1,
        'kd':'python'
    }
    response = requests.post(url,headers=headers,data=data)
    # 如果返回的是json数据那么这个方法会自动load程字典
    # 爬取不到数据,可能被识别出了我是一个爬虫,用selenium
    print(response.json())

def main():
    request_liet_page()

if __name__ == '__main__':
        main()
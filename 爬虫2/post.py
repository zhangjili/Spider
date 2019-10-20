import requests
data = {
    'first':'true',
    'pn': '1',
    'kd': 'python'
}
headers = {
    'Referer':'https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?labelWords=sug&fromSearch=true&suginput=python',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
    'Cookie':'Cookie: user_trace_token=20191003132919-159f6844-f2ad-4445-a5eb-e5e49a5ff041; _ga=GA1.2.1739252142.1570080564; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=; LGSID=20191003132925-c3690d19-e59e-11e9-97c5-525400f775ce; LGUID=20191003132925-c3691152-e59e-11e9-97c5-525400f775ce; gate_login_token=9ae944a3c0713b7c0a0dedf7bb0056749c9c76ff787209e1c6e2a7fef60026e3; LG_HAS_LOGIN=1; _putrc=43F4E85C399E563B123F89F2B170EADC; JSESSIONID=ABAAABAAAIAACBIBC843687AA6C29A78EB873B37FD90CEA; login=true; hasDeliver=0; _gid=GA1.2.1287896488.1570080627; WEBTJ-ID=20191003133648-16d901eea54189-0934ff7efa770c-67e153a-2073600-16d901eea558c0; privacyPolicyPopup=false; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_search; sajssdk_2015_cross_new_user=1; X_MIDDLE_TOKEN=e5cccb491c88abff2f59d9b17db635e5; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d901f7edb6b2-07ba68e6c9340d-67e153a-2073600-16d901f7edc897%22%2C%22%24device_id%22%3A%2216d901f7edb6b2-07ba68e6c9340d-67e153a-2073600-16d901f7edc897%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570080564,1570081636; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B72650; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; X_HTTP_TOKEN=fbcf36135c9f2e1f1571800751c80a250f5007b7fc; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570081755; LGRID=20191003134916-890f8f76-e5a1-11e9-97c5-525400f775ce; SEARCH_ID=ec6eae3906b74b47b558fabc3790b87e'
}
proxy ={
    'http': '110.86.136.189:9999'
}
response = requests.post("https://www.lagou.com"
                         "/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&ne"
                         "edAddtionalResult=false",data=data,headers=headers)
print(response.text)

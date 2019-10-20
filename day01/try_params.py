import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/54.0.2840.99 Safari/537.36"}
p = {"wd":"传智播客"}
# url_temp="http://www.baidu.com/s?"
# url_temp="http://www.baidu.com/s"也可以
# {}用来站位
url = "http://www.baidu.com/s?wd={}".format("传智播客")
r = requests.get(url,headers=headers)
print(r.status_code)
print(r.request.url)
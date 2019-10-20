import requests
# response = requests.get("http://www.baidu.com")
# print(response.content.decode('utf-8'))
# print(response.encoding)
params = {
    'wd': "中国"
}

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}

response = requests.get("https://www.baidu.com/s",params=params,headers=headers)
with open("中国.html",'w',encoding='utf-8') as f:
    f.write(response.content.decode('utf-8 '))
print(response.url)
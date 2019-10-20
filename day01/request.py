import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/54.0.2840.99 Safari/537.36"}
response=requests.get("http://www.baidu.com",headers=headers)
print(response.status_code)
print(response.headers)
print(response.request.url)
print(response.request.headers)
print(response.content.decode())
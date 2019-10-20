# coding=utf-8
import requests

# 发送请求
response = requests.get("https://www.baidu.com/img/bd_logo1.png")

# 保存 b 表示以二进制的形式来进行写,图片是二进制的内容
with open("a.png", "wb") as f:
    f.write(response.content)

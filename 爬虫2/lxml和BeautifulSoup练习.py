# encoding:utf-8
from bs4 import BeautifulSoup
from lxml import etree
import requests
import os
from urllib import request
import threading
from queue import Queue
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}
response = requests.get("https://fabiaoqing.com/biaoqing/lists/page/",headers=headers)
text = response.text
# html = etree.HTML(text)
# a = html.xpath("//img")
# print(a)
# for i in a:
#     # 可以这么写 也可以用xpath写
#     b = i.get("data-original")
#     # b = i.xpath(".//@href")[0]
#     print(b)

# BeautifulSoup 自动将输入文档转换为 Unicode 编码，输出文档转换为 utf-8 编码。你不需要考虑编码方式
# lxml HTML 解析器 BeautifulSoup (markup, “lxml”) 速度快、文档容错能力强需要安装 C 语言库
# lxml XML 解析器 BeautifulSoup (markup, “xml”) 速度快、唯一支持 XML 的解析器需要安装 C 语言库
# html5libBeautifulSoup (markup, “html5lib”) 最好的容错性、以浏览器的方式解析文档、生成 HTML5 格式的文档速度慢、不依赖外部扩展
soup = BeautifulSoup(text,"lxml")
# 用attrs来获取标签的属性,但是也可以用get()来获取  你快乐吗
a = soup.find_all('img',attrs = {
    'data-original':True
})[1:-1]
# for i in a:
#     # Beautiful 中也可以使用get()来获取属性的值
#     src = i.get('data-original')
#     print(src)
# for i in a:
#     print(i.attrs['data-original'])
# # 网站的标题
# print(soup.title)
# print(a)

def download(q):
    a,b,c = q.get()
    print(a,b,c)
    request.urlretrieve(a, c)
    if q.empty():
        exit()

# 有问题
if __name__ == '__main__':
    q = Queue()
    img_list = soup.find_all('img', class_='ui image lazy')
    for img in img_list:
        image_url = img.get('data-original')
        image_name = img.get('title')
        image_suffix = os.path.splitext(image_url)[-1]
        file_name = "images/" + image_name + image_suffix
        q.put((image_url, image_name, file_name))
        # print('下载图片： ', image_name)
        # print(file_name)
    for i  in  range(45):
        t = threading.Thread(target=download,args=(q,))
        t.start()
    
    






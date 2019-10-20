# encoding: utf-8
import requests
import re

def parse_page(url):
    headers ={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    # print(response.text.encode('GBK','ignore').decode('GBk'))
    text = response.text.encode('GBK','ignore').decode('GBk')
    # re.DOTALL可以让.匹配到\n re.S 与 re.DOTALL的效果是一样的
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    # print(titles)
    dynasties = re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    # print(dynasties)
    authors = re.findall(r'<p\sclass="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    # print(authors)
    contnets_tag = re.findall(r'<div class="contson".*?>(.*?)</div>',text,re.DOTALL)
    contents=[]
    for content1 in contnets_tag:
        x =re.sub(r'<.*?>',"",content1)
        # print(x.strip())
        contents.append(x.strip())
     
    poems = []
    for value in (titles,dynasties,authors,contents):
        title,dynasty,author,content = value
        # print(title,dynasty,author,content)
        poem = {
            'title':title,
            'dynasty':dynasty,
            'author':author,
            'content':content
        }
        poems.append(poem)
    for poem in poems:
        print(poem)
        # print("**"*30)
        
def main():
    # url = 'https://www.gushiwen.org/default.aspx?page=2'
    for x in range(1,11):
        url ='https://www.gushiwen.org/default.aspx?page={}'.format(x)
        parse_page(url)
    
    
if __name__ == '__main__':
    main()
    
# -*- coding: gbk -*-
import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar

ALL_DATA = []
def parse_page(url):
    headers = { 'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
    response = requests.get(url,headers=headers)
    # print(response.content.decode('utf-8'))
    text = response.content.decode('utf-8')
    # 当遇到标签不完整的时候,可以使用HTML5lib解析,因为HTML5lib可以自动补齐标签,香港,澳门缺少</table>标签
    # soup = BeautifulSoup(text.replace('&nbsp;', ' '),'lxml')
    soup = BeautifulSoup(text.replace('&nbsp;', ' '), 'html5lib')
    conMidtab = soup.find('div',class_='conMidtab')
    # print(conMidtab)
    tables = conMidtab.find_all('table')
    for table in tables:
        # trs 返回的是列表
        trs = table.find_all('tr')[2:]
        # trs是列表,每个tr是一项,也就是说每个tr之间有逗号
        for index,tr in enumerate(trs):
            # print(index,tr)
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({"city":city,"min_temp":int(min_temp)})
            # print({"city":city,"min_temp":min_temp})
         
    
    
    
def main():
    urls=[
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]
    for url in urls:
        parse_page(url)
        
    # 分析数据
    # 根据最低气温排序
    ALL_DATA.sort(key=lambda data:data['min_temp'])
    print(ALL_DATA)
    data = ALL_DATA[0:10]
    # 取名字
    cities = list(map(lambda x:x['city'],data))
    # 取气温
    temps = list(map(lambda x:x['min_temp'],data))
    print(cities,temps)
    chart = Bar()
    chart.add_xaxis(cities)
    chart.add_yaxis('',temps)
    chart.render('./temperature.html')
    # 提取所有的城市名字
    # 这样写麻烦
    # cities = []
    # for city_temp in ALL_DATA:
    #     city = city_temp['city']
    #     cities.append(city)
    
if __name__ == '__main__':
    main()
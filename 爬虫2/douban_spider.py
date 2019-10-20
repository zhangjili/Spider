import requests
from lxml import etree

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
    #   "Referer":'https://movie.douban.com/cinema/nowplaying/beijing/'
}
url = 'https://movie.douban.com/cinema/nowplaying/beijing/'

response = requests.get(url, headers=headers)
# print(response.text)
text = response.text
# html 是一个<Element html at 0x1ac50970a88>类型
html = etree.HTML(text)
# 有两个lists
ul = html.xpath("//ul[@class='lists']")[0]
# print(ul)
lis = ul.xpath("./li")
movies = []
for li in lis:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    thumbnail = li.xpath(".//img/@src")[0]
    movie = {
        'title': title,
        'score': score,
        'duration': duration,
        'retion': duration,
        'region': region,
        'director': director,
        'actors': actors,
        'thumbnail': thumbnail
    }
    movies.append(movie)
print(movies)

from lxml import etree
import requests

HEADERS = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
}
BASE_DOMAIN = "http://www.dytt8.net"


def get_detail_urls(url):
    response = requests.get(url, headers=HEADERS)
    # print(response.text/) #乱码
    # print(response.content.decode('gbk','ignore'))
    # 遇到不能解码的就直接忽略
    text = response.content.decode('gbk', 'ignore')
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    # for detail_url in detail_urls:
    #     print(BASE_DOMAIN+detail_url)
    # 把detail_urls的每一项赋给url,然后 BASE_DOMAIN+url构成完整路径
    detail_urls = map(lambda url: BASE_DOMAIN + url, detail_urls)
    # print(detail_urls)
    return detail_urls


def parse_detail(url):
    movie = {}
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk', 'ignore')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]
    screenshot = imgs[1]
    infos = zoomE.xpath(".//text()")
    
    # print(infos)
    # infos返回的是列表的形式,页面内的一行是列表中的一项
    def parse_info(info, rule):
        return info.replace(rule, "").strip()
    
    # 列表可以放在enumerate中,返回的是索引和内容
    for index, info in enumerate(infos):
        # print(info)
        if info.startswith("◎年　　代"):
            info = parse_info(info, "◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info, "◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info, "◎类　　别")
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info, "◎豆瓣评分")
            movie['category'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info, "◎片　　长")
            movie['category'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info, "◎导　　演")
            movie['category'] = info
        elif info.startswith("◎主　　演"):
            info = parse_info(info, "◎主　　演")
            actors = [info]
            for x in range(index + 1, len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            info = parse_info(info, "◎简　　介")
            mv = []
            for x in range(index + 1, len(infos)):
                profile = infos[x].strip()
                if profile.startswith("【下载地址】"):
                    break
                mv.append(profile)
                # 把列表转化为字典,并去除最后一个空格
            movie['profile'] = "".join(mv).strip()
            # print(profile)
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url
    movie['title'] = title
    movie['cover'] = cover
    movie['screenshot'] = screenshot
    
    return movie


def spider():
    base_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    for x in range(1, 8):
        movies = []
        url = base_url.format(x)
        # print(url)
        detail_urls = get_detail_urls(url)
        for detail in detail_urls:
            detail_movies = parse_detail(detail)
            movies.append(detail_movies)
            
            print(movies)


if __name__ == '__main__':
    spider()

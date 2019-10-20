import requests


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/63.0.3239.84 Safari/537.36"}

    def get_url_list(self):
        return [self.url_temp.format(i * 50) for i in range(10)]

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, page_num):
        file_path = "{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="utf8") as f:
            f.write(html_str)

    def run(self):
        # 构造url列表
        url_list = self.get_url_list()
        # 遍历
        for url in url_list:
            html_str = self.parse_url(url)
            # 保存
            page_num = url_list.index(url) + 1
            self.save_html(html_str, page_num)

if __name__ == '__main__':
    tieba_spider = TiebaSpider("李毅")
    tieba_spider.run()

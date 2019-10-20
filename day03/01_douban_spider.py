# coding=utf-8
import requests
import json


class DoubanSpider:
    def __init__(self):
        self.url_temp= " https://movie.douban.com/j/search_subjects?" \
                             "type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}",

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}

    def parse_url(self, url):  # 发送请求，获取响应
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, json_str):  # 提取是数据
        dict_ret = json.loads(json_str)
        print(dict_ret)
        content_list = dict_ret["subjects"]
        # total = dict_ret["total"]
        return content_list

    def save_content_list(self, content_list):  # 保存
        with open("douban.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")  # 写入换行符，进行换行
        print("保存成功")

    def run(self):  # 实现主要逻辑

        num = 0
        # total = 100  # 假设有第一页

        # 1.start_url

        url =" https://movie.douban.com/j/search_subjects?" \
                             "type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=60"
        # 2.发送请求，获取响应
        json_str = self.parse_url(url)
        # 3.提取是数据
        content_list = self.get_content_list(json_str)

        # 4.保存
        self.save_content_list(content_list)
    # if len(content_list)<18:
    #     break
    # 5.构造下一页的url地址,进入循环
        num += 20


if __name__ == '__main__':
    douban_spider = DoubanSpider()
    douban_spider.run()

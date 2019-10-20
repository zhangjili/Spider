# coding=utf-8
from selenium import webdriver
import time

class DouyuSpider:
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\10366\\chromedriver.exe")

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@class='layout-Cover-list']/li")
        print(li_list)
        content_list = []
        for li in li_list:
            item = {}
            # item["room_img"] = li.find_element_by_xpath(".//div[@class='DyListCover-imgWrap']/div/img").get_attribute("src")
            # print(item["room_img"])
            item["room_title"] = li.find_element_by_xpath(".//div[@class='DyListCover HeaderCell is-href']//div["
                                                          "@class='DyListCover-content']//h3").get_attribute("title")
            # item["room_cate"] = li.find_element_by_xpath(".//span[@class='tag ellipsis']").text
            # item["anchor_name"] = li.find_element_by_xpath(".//span[@class='dy-name ellipsis fl']").text
            # item["watch_num"] = li.find_element_by_xpath(".//span[@class='dy-num fr']").text
            # print(item)
            content_list.append(item)
        # 获取下一页的元素
        next_url = self.driver.find_elements_by_xpath("//span[@class='dy-Pagination-item-custom']")
        next_url = next_url[0] if len(next_url) > 0 else None
        print("*"* 50)
        print(next_url)
        return content_list, next_url

    def save_content_list(self, content_list):
        pass

    def run(self):  # 实现主要逻辑
        # 1.start_url
        # 2.发送请求，获取响应
        self.driver.get(self.start_url)
        # 3.提取数据，提取下一页的元素
        content_list, next_url = self.get_content_list()
        # 4.保存数据
        self.save_content_list(content_list)
        # 5.点击下一页元素，循环
        while next_url is not None:
            next_url.click()
            time.sleep(6)
            content_list, next_url = self.get_content_list()
            self.save_content_list(content_list)


if __name__ == '__main__':
    douyu = DouyuSpider()
    douyu.run()

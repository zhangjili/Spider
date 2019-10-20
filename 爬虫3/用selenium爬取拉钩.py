# coding=utf-8
# 存在的问题 : 点击不到下一页
import re
import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class LagouSpider(object):
    driver_path = r'C:\Users\10366\chromedriver.exe'
    
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.positions = []
        # print(self.positions)
        
    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='pager_container']/span[last()]"))
            )
            # print(source)
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
            # 下拉框
            # self.driver.execute_script("arguments[0].scrollIntoView(false);", next_btn)
            # js = "window.scrollTo(285, 897)"
            # self.driver.execute_script(js)
            
            if "pager_next_disabled" in next_btn.get_attribute("class"):
                break
            else:
                next_btn.click()
            time.sleep(1)
    
    def parse_list_page(self, source):
        pass
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            # print(link)
            self.request_detail_page(link)
            time.sleep(1)
    
    def request_detail_page(self, url):
        # 不能覆盖原来的页面,因为要在首页点击下一页
        # self.driver.get(url)
        self.driver.execute_script("window.open('%s')" % url)
        # 切换过去
        self.driver.switch_to.window(self.driver.window_handles[1])
        
        WebDriverWait(self.driver, timeout=5).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='name']"))
        )
        source = self.driver.page_source
        # print(source)
        self.parse_detail_page(source)
        # 保证只有两个窗口,关掉详情页的页面
        self.driver.close()
        # 切换会首页
        self.driver.switch_to.window(self.driver.window_handles[0])
    
    def parse_detail_page(self, source):
        html = etree.HTML(source)
        position_name = html.xpath("//span[@class='name']/text()")[0]
        job_request_spans = html.xpath("//dd[@class='job_request']//span")
        salary = job_request_spans[0].xpath(".//text()")[0].strip()
        city = job_request_spans[1].xpath(".//text()")[0].strip()
        city = re.sub(r"[\s/]", "", city)
        work_years = job_request_spans[2].xpath(".//text()")[0].strip()
        work_years = re.sub(r"[\s/]", "", work_years)
        education = job_request_spans[3].xpath(".//text()")[0].strip()
        education = re.sub(r"[\s/]", "", education)
        desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
        position = {
            # 因为控制台是用gbk解码的,所以可以先用gbk编码,忽略不能解码的类型,然后再解码
            'name': position_name.encode('GBK','ignore').decode('GBk'),
            'salary': salary.encode('GBK','ignore').decode('GBk'),
            'city': city.encode('GBK','ignore').decode('GBk'),
            'work_years': work_years.encode('GBK','ignore').decode('GBk'),
            'education': education.encode('GBK','ignore').decode('GBk'),
            'desc': desc.encode('GBK','ignore').decode('GBk')
        }
        self.positions.append(position)
        print(position )

if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()

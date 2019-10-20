# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path=r"C:\Users\10366\chromedriver.exe")
driver.get('https://www.baidu.com')
# 行为链,爬虫一般不用,测试时用的比较多
for cookie in driver.get_cookies():
    print(cookie)
print(driver.get_cookie("PSTM"))
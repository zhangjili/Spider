# coding=utf-8
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://171.39.42.45:8123")

driver = webdriver.Chrome(executable_path=r"C:\Users\10366\chromedriver.exe",chrome_options=op4)
driver.get('https://www.baidu.com')

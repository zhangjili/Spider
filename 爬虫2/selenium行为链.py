# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path=r"C:\Users\10366\chromedriver.exe")
driver.get('https://www.baidu.com')
# 行为链,爬虫一般不用,测试时用的比较多
inputTag = driver.find_element_by_id('kw')
button = driver.find_element_by_id('su')

actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag,'python')
actions.move_to_element(button)
actions.click(button)
actions.perform()
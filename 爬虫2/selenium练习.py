# -*- coding: gbk -*-
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\Users\10366\chromedriver.exe")
driver.get('https://www.baidu.com')
# print(driver.page_source) �������
inputTag = driver.find_element_by_id('kw')
# inputTag1 = driver.find_element_by_name('wd')
# inputTag2 = driver.find_element_by_class_name('s_ipt')
# inputTag3 = driver.find_element_by_xpath("//input[@id='kw']")
# inputTag.send_keys('python')
button = driver.find_element_by_id('su')
print(type(button))
print(button.get_attribute("value"))
button.click()
# �������
driver.save_screenshot('baidu.com')
# ѡ��checkbox ��click����
# ������
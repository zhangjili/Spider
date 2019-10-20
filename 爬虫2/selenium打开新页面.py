# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path=r"C:\Users\10366\chromedriver.exe")
driver.get('https://www.baidu.com')
# 再打开一个窗口
driver.execute_script("window.open('https://www.douban.com/')")
# 但是还是停留在原来的百度的页面
# 切换到豆瓣的页面
driver.driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
# 虽然在窗口中切换到了新的页面,但是driver中还没有切换


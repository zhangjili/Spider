from selenium import webdriver
# Keys 类提供所有的键盘按键操作
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Users\\10366\\chromedriver.exe')
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()
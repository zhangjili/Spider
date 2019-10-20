import time
from selenium import webdriver


def login():
    acount_num = input('请输入账号:\n')
    passwd_str = input('请输入密码:\n')
    driver = webdriver.Chrome(executable_path="C:\\Users\\10366\\chromedriver.exe")
    url = 'http://mail.163.com/'
    driver.get(url)
    time.sleep(2)

    # 使用CSSSelector正则匹配头部
    elem = driver.find_element_by_css_selector("iframe[id^='x-URS-iframe']")
    # 163登陆框是使用iframe进行嵌套的，所以需要先切换到该iframe
    driver.switch_to.frame(elem)

    acount = driver.find_element_by_name('email')
    acount.clear()
    acount.send_keys(acount_num)

    passwd = driver.find_element_by_name('password')
    passwd.clear()
    passwd.send_keys(passwd_str)

    time.sleep(2)
    click_button = driver.find_element_by_id('dologin')
    click_button.click()
    time.sleep(2)
    cur_cookies = driver.get_cookies()[0]
    return cur_cookies


if __name__ == '__main__':
    login()

#!/usr/bin/env python
#encoding=utf-8

from selenium import webdriver
import requests
import lxml
import time

url = 'https://processon.com/login?f=index'
user = '519419914@qq.com'
passwd = 'xxx'

try:
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html
    browser = webdriver.Chrome()
    browser.get(url)
    browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    btm1.click()

    browser.find_element_by_xpath('//*[@id="username"]').send_keys(user))
    browser.find_element_by_id('password').send_keys(passwd)
    time.sleep(1)
    browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()

    # 获取cookies
    cookies = browser.get_cookies() 
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:    
    browser.close()
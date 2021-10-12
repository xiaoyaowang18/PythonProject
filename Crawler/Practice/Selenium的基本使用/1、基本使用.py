# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 15:27
# @Author  : wanghc
# @File    : 1、基本使用.py
# @Software: PyCharm

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

'''
Selenium 是一个自动化测试工具，利用它可以驱动浏览器执行特定的动作，如点击、下拉等操作，
同时还可以获取浏览器当前呈现的页面源代码，做到可见即可爬。
对于一些使用 JavaScript 动态渲染的页面来说，此种抓取方式非常有效。
'''

browser = webdriver.Chrome()  # 声明浏览器对象
try:
    browser.get('https://www.baidu.com')  # 访问页面
    input = browser.find_element_by_id('kw')  # 查找到搜索框节点
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)  # 打印出源代码
finally:
    browser.close()

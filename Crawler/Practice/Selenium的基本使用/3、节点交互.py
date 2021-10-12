# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 16:32
# @Author  : wanghc
# @File    : 3、节点交互.py
# @Software: PyCharm

'''
Selenium 可以驱动浏览器来执行一些操作，或者说可以让浏览器模拟执行一些动作。
比较常见的用法有：输入文字时用 send_keys 方法，清空文字时用 clear 方法，点击按钮时用 click 方法。
'''

from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()
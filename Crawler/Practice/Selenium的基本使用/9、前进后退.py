# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 18:04
# @Author  : wanghc
# @File    : 9、前进后退.py
# @Software: PyCharm

'''
这里我们连续访问 3 个页面，然后调用 back  方法回到第 2 个页面，
接下来再调用 forward 方法又可以前进到第 3 个页面。
'''
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()

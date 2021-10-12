# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 16:43
# @Author  : wanghc
# @File    : 5、执行JavaScript.py
# @Software: PyCharm

'''
Selenium API 并没有提供实现某些操作的方法，比如，下拉进度条。
但它可以直接模拟运行 JavaScript，此时使用 execute_script 方法即可实现
'''

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')

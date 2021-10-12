# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 18:10
# @Author  : wanghc
# @File    : 12、异常处理.py
# @Software: PyCharm

'''
在使用 Selenium 的过程中，难免会遇到一些异常，例如超时、节点未找到等错误，一旦出现此类错误，程序便不会继续运行了。
这里我们可以使用 try except 语句来捕获各种异常。
关于更多的异常类，可以参考官方文档：
http://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions。
'''

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()

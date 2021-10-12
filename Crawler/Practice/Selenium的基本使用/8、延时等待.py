# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 17:06
# @Author  : wanghc
# @File    : 8、延时等待.py
# @Software: PyCharm

'''
在 Selenium 中，get 方法会在网页框架加载结束后结束执行，此时如果获取 page_source，
可能并不是浏览器完全加载完成的页面，如果某些页面有额外的 Ajax 请求，我们在网页源代码中也不一定能成功获取到。
所以，这里需要延时等待一定时间，确保节点已经加载出来。

这里等待的方式有两种：一种是隐式等待，一种是显式等待。

更多详细的等待条件的参数及用法介绍可以参考官方文档：
http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions。
'''

'''
1、当使用隐式等待执行测试的时候，如果 Selenium 没有在 DOM 中找到节点，将继续等待，
超出设定时间后，则抛出找不到节点的异常。换句话说，隐式等待可以在我们查找节点而节点并没有立即出现的时候，
等待一段时间再查找 DOM，默认的时间是 0。
'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(10)  # 隐式等待
browser.get('https://dynamic2.scrape.center/')
input = browser.find_element_by_class_name('logo-image')
print(input)

'''
2、显式等待方法，它指定要查找的节点，然后指定一个最长等待时间。
如果在规定时间内加载出来了这个节点，就返回查找的节点；如果到了规定时间依然没有加载出该节点，则抛出超时异常。
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)  # 引入 WebDriverWait 这个对象，指定最长等待时间
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))  # 调用它的 until() 方法，传入要等待条件 expected_conditions
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)

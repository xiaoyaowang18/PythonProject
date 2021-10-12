# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 17:01
# @Author  : wanghc
# @File    : 7、切换Frame.py
# @Software: PyCharm


import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

'''
网页中有一种节点叫作 iframe，也就是子 Frame，相当于页面的子页面，它的结构和外部网页的结构完全一致。
Selenium 打开页面后，默认是在父级 Frame 里面操作，而此时如果页面中还有子 Frame，
Selenium 是不能获取到子 Frame 里面的节点的。这时就需要使用 switch_to.frame 方法来切换 Frame。
'''
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO LOGO')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)
# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 15:49
# @Author  : wanghc
# @File    : 2、查找节点.py
# @Software: PyCharm

from selenium import webdriver

'''
1、单个节点 
所有获取单个节点的方法：
find_element_by_id 

find_element_by_name 

find_element_by_xpath 

find_element_by_link_text 

find_element_by_partial_link_text 

find_element_by_tag_name 

find_element_by_class_name 

find_element_by_css_selector
'''

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')  # 根据 id 获取
input_second = browser.find_element_by_css_selector('#q')  # 根据CSS 选择器获取
input_third = browser.find_element_by_xpath('//*[@id="q"]')  # 根据XPath 获取
print(input_first, input_second, input_third)
browser.close()


'''
2、多个节点
find_elements_by_id 

find_elements_by_name 

find_elements_by_xpath 

find_elements_by_link_text 

find_elements_by_partial_link_text 

find_elements_by_tag_name 

find_elements_by_class_name 

find_elements_by_css_selector
'''
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)
browser.close()
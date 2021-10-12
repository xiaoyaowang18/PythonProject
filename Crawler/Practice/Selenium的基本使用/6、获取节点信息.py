# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 16:44
# @Author  : wanghc
# @File    : 6、获取节点信息.py
# @Software: PyCharm

'''
获取属性，通过get_attribute方法
获取文本，通过text属性
获取ID、位置、标签名、大小  通过id、location、tag_name、size
'''
from selenium import webdriver
browser = webdriver.Chrome()
url = 'https://dynamic2.scrape.center/'
browser.get(url)
logo = browser.find_element_by_class_name('logo-image')
input = browser.find_element_by_class_name('logo-title')
print(logo)
print(logo.get_attribute('src'))
print(input.text)
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
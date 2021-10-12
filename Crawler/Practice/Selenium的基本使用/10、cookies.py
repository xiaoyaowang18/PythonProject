# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 18:05
# @Author  : wanghc
# @File    : 10、cookies.py
# @Software: PyCharm

'''
访问知乎，加载完成后，浏览器实际上已经生成 Cookies 了。接着，调用 get_cookies 方法获取所有的 Cookies。
然后，我们再添加一个 Cookie，这里传入一个字典，有 name、domain 和 value 等内容。
接下来，再次获取所有的 Cookies，可以发现，结果会多出这一项新加的 Cookie。
最后，调用 delete_all_cookies 方法删除所有的 Cookies。再重新获取，发现结果就为空了。
'''

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())

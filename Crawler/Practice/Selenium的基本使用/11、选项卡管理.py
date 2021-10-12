# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 18:08
# @Author  : wanghc
# @File    : 11、选项卡管理.py
# @Software: PyCharm

'''
首先访问百度，然后调用 execute_script 方法，这里我们传入 window.open 这个 JavaScript 语句新开启一个选项卡，
然后切换到该选项卡，调用 window_handles 属性获取当前开启的所有选项卡，后面的参数代表返回选项卡的代号列表。
要想切换选项卡，只需要调用 switch_to.window 方法即可，其中的参数是选项卡的代号。
这里我们将第 2 个选项卡代号传入，即跳转到第 2 个选项卡，接下来在第 2 个选项卡下打开一个新页面，
如果你想要切换回第 2 个选项卡，只需要重新调用 switch_to.window 方法，再执行其他操作即可。
'''
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://python.org')

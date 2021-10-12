# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 16:41
# @Author  : wanghc
# @File    : 4、动作链.py
# @Software: PyCharm

'''
在上面的实例中，一些交互动作都是针对某个节点执行的。比如，对于输入框，我们调用它的输入文字和清空文字方法；
对于按钮，我们调用它的点击方法。其实，还有另外一些操作，它们没有特定的执行对象，比如鼠标拖拽、键盘按键等，
这些动作用另一种方式来执行，那就是动作链。

比如，现在我要实现一个节点的拖拽操作，将某个节点从一处拖拽到另外一处，可以这样实现
'''

from selenium import webdriver
from selenium.webdriver import ActionChains
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
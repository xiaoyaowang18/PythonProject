# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 18:12
# @Author  : wanghc
# @File    : 13、反屏蔽.py
# @Software: PyCharm


'''
现在很多网站都加上了对 Selenium 的检测，来防止一些爬虫的恶意爬取。
即如果检测到有人在使用 Selenium 打开浏览器，那就直接屏蔽。

其大多数情况下，检测基本原理是检测当前浏览器窗口下的 window.navigator 对象是否包含 webdriver 这个属性。
因为在正常使用浏览器的情况下，这个属性是 undefined，然而一旦我们使用了 Selenium，
Selenium 会给 window.navigator 设置 webdriver 属性。很多网站就通过 JavaScript 判断如果 webdriver 属性存在，
那就直接屏蔽。
'''

from selenium import webdriver
from selenium.webdriver import ChromeOptions

'''
在 Selenium 中，我们可以使用 CDP（即 Chrome Devtools-Protocol，Chrome 开发工具协议）来解决这个问题，
通过 CDP 我们可以实现在每个页面刚加载的时候执行 JavaScript 代码，执行的 CDP 方法叫作 Page.addScriptToEvaluateOnNewDocument，
然后传入上文的 JavaScript 代码即可，这样我们就可以在每次页面加载之前将 webdriver 属性置空了。
另外我们还可以加入几个选项来隐藏 WebDriver 提示条和自动化扩展信息
'''
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=option)
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
})
browser.get('https://antispider1.scrape.center/')

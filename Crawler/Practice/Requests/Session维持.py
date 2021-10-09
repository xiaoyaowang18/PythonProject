# -*- coding: utf-8 -*-
# @Time    : 2021/9/29 16:30
# @Author  : wanghc
# @File    : Session维持.py
# @Software: PyCharm

import requests

'''
在 requests 中，如果直接利用 get 或 post 等方法的确可以做到模拟网页的请求，但是这实际上是相当于不同的 Session，相当于你用两个浏览器打开了不同的页面。

设想这样一个场景，第一个请求利用 post 方法登录了某个网站，第二次想获取成功登录后的自己的个人信息，你又用了一次 get 方法去请求个人信息页面。实际上，这相当于打开了两个浏览器，是两个完全不相关的 Session，能成功获取个人信息吗？当然不能。

有人会问，我在两次请求时设置一样的 Cookies 不就行了？可以，但这样做起来很烦琐，我们有更简单的解决方法。

解决这个问题的主要方法就是维持同一个 Session，相当于打开一个新的浏览器选项卡而不是新开一个浏览器。但我又不想每次设置 Cookies，那该怎么办呢？这时候就有了新的利器 ——Session 对象。
'''

import requests


s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')

r = s.get('http://httpbin.org/cookies')

print(r.text)

'''
利用session，可以做到模拟同一个Session而不用担心Cookies的问题，它通常用于模拟登录成功之后的下一步操作。
'''
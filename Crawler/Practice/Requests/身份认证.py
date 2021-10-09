# -*- coding: utf-8 -*-
# @Time    : 2021/9/29 17:27
# @Author  : wanghc
# @File    : 身份认证.py
# @Software: PyCharm


import requests

'''
这个网站启用了基本身份认证，英文叫作 HTTP Basic Access Authentication，它是一种用来允许网页浏览器或其他客户端程序在请求时提供用户名和口令形式的身份凭证的一种登录验证方式。

如果遇到了这种情况，怎么用 reqeusts 来爬取呢，当然也有办法。

我们可以使用 requests 自带的身份认证功能，通过 auth 参数即可设置
'''

import requests

from requests.auth import HTTPBasicAuth



r = requests.get('https://static3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))

print(r.status_code)


'''
也可以简写
'''

r = requests.get('https://static3.scrape.center/', auth=('admin', 'admin'))

print(r.status_code)

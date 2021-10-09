# -*- coding: utf-8 -*-
# @Time    : 2021/9/29 16:40
# @Author  : wanghc
# @File    : ssl证书认证.py
# @Software: PyCharm


import requests
import logging

'''
现在很多网站都要求使用 HTTPS 协议，但是有些网站可能并没有设置好 HTTPS 证书，或者网站的 HTTPS 证书不被 CA 机构认可，
这时候，这些网站可能就会出现 SSL 证书错误的提示。

比如这个示例网站：https://static2.scrape.center/。

'''


# response = requests.get('https://static2.scrape.center/')
#
# print(response.status_code)


'''
使用verify参数控制是否验证证书，将其设置为False，在请求时就不会再验证证书是否有效。
并屏蔽警告
'''



logging.captureWarnings(True)
response = requests.get('https://static2.scrape.center/',verify = False)

print(response.status_code)
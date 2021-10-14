# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 3、其他请求类型.py
@time: 2021/10/13 21:56
"""

session.post('http://httpbin.org/post', data=b'data')
session.put('http://httpbin.org/put', data=b'data')
session.delete('http://httpbin.org/delete')
session.head('http://httpbin.org/get')
session.options('http://httpbin.org/get')
session.patch('http://httpbin.org/patch', data=b'data')

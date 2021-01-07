# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 3.约定俗成.py
@time: 2021/1/7 22:26
"""


class JJ:
    def __init__(self):
        self._a = 3


j = JJ()

print(j._a)

j._a = 4

print(j._a)

print(j.__dict__)


'''
发现以上操作都可以。
单下划线是一种惯用方法，标记此成员是私有的，但是解释器不做任何处理

一般都是库的提供者告诉我们使用的人，这个是不要动的。
'''
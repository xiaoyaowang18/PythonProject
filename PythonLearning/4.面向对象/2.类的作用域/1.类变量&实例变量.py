# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 1.类变量&实例变量.py
@time: 2021/1/6 20:35
"""


class E:
    NAME = 'E'

    def __init__(self, name):
        self.name = name


e = E('e')

print(E.NAME)  # E
print(e.NAME)  # E
print(e.name)  # e

'''
在类下面定义的变量，叫做类变量，是类的直接下级作用域
可以看到，类变量对类和实例都可见。

关联到实例的变量叫做实例变量
'''


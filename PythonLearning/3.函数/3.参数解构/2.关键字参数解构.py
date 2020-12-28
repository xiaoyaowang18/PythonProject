# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 2.关键字参数解构.py
@time: 2020/12/28 22:48
"""


def add(x, y):
    ret = x + y
    print('{} + {} = {}'.format(x, y, ret))
    return ret


d = {'x': 1, 'y': 2}

add(**d)

'''
关键字参数解构，加2个星号，可以把字典解构成关键字参数
'''

'''
参数解构的2种形式：
1.一个星号：解构的对象是一个可迭代对象，解构的结果是位置参数
2.二个星号：解构的对象是一个字典，解构的结果是关键字参数
'''

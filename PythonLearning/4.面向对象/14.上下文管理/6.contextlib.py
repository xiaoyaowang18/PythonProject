# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 23:09
# @Author  : wanghc
# @File    : 6.contextlib.py
# @Software: PyCharm


'''
通常上下文管理需要写一个类，但有时候一个简单的逻辑，并不需要写一个类
'''

import contextlib


@contextlib.contextmanager
# 可以把生成器转换成我们的上下文管理
def context():
    # 必须要有try  里面是yield  然后加上finally, try上面是正常逻辑
    print('enter context')  # 初始化部分  相当于__enter__
    try:
        yield 'hhh'  # 相当于__enter__返回值
    finally:
        print('exit context')  # 相当于__exit__方法


with context() as c:
    print(c)

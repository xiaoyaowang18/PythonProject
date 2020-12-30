# -*- coding: utf-8 -*-
# @Time    : 2020/12/30 17:19
# @Author  : wanghc
# @File    : 1.定义.py
# @Software: PyCharm


def count(base):
    def inc(x=1):
        nonlocal base
        base += x
        return base

    return inc


# 这种返回值是一个函数或者参数是函数的情况，称为高阶函数。
inc = count(3)  # 函数赋值
print(inc())
print(inc())

'''
第一种情况：返回值是函数
第二种情况: 参数是函数

这两种情况的函数，叫做高阶函数。
在python中一切皆对象，变量是对象，函数也是对象，并且它可以像普通对象一样赋值，作为参数，作为返回值。
'''

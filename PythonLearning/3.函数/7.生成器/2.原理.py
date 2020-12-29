# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 2.原理.py
@time: 2020/12/30 1:02
"""


def gen():
    print('a')
    yield 1
    print('b')
    yield 2
    return 3


g = gen()
print(type(g))  # <class 'generator'>  g是一个生成器

print(next(g))  # 打印 a  1   next调用后发现执行到第一个yield，他就停止执行了。
print(next(g))  # 打印 b  2   现场被保留了，直接从yield 1 后面开始执行。
print(next(g))  # 报错了，没有更多yield的时候，抛出stopiteration异常。异常值就是gen函数的返回值

'''
总结：带yield语句的函数称为生成器函数，生成器函数的返回值是生成器。

特点：
1.生成器函数执行的时候，不会执行函数体
2.当next生成器的时候，当前代码执行到第一个yield关键字为止，会弹出值，并暂停函数
3.当再次next生成器的时候，从上次暂停处开始往下执行
4.当没有多余的yield的时候，会抛出StopInteration异常，如果函数有返回值，异常的value就是函数的返回值。
'''

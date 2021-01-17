# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 11:38
# @Author  : wanghc
# @File    : 7.异常的传递.py
# @Software: PyCharm


def f1():
    raise Exception()


def f2():
    f1()


f2()

'''
当抛出异常的时候，如果没有捕获处理，会继续传递到上层作用域，直到最顶层，如果到最顶层还没有处理，会中断当前线程

有了这个异常的传递行为，如何捕获异常？
'''
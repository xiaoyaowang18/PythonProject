# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 14:35
# @Author  : wanghc
# @File    : 1.实例方法.py
# @Software: PyCharm


class A:
    def print(self):
        print('instance method')


a = A()

a.print()

A.print()  # TypeError: print() missing 1 required positional argument: 'self'

'''
实例调用实例方法的时候会自动传入self参数，self为实例本身
实例方法只能由实例调用。
'''

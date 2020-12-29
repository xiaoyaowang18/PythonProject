# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 2.匿名函数的调用.py
@time: 2020/12/30 0:16
"""

# 将整个函数表达式赋值给一个变量  f

f = lambda x: x + 1

print(type(f))  # <class 'function'>  可以看到f是一个函数类型

# 既然f是一个函数对象，那么可以调用它了

print(f(5))  # 6

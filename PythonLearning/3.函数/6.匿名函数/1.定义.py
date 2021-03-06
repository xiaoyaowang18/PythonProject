# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 1.定义.py
@time: 2020/12/30 0:11
"""

# 所谓的匿名函数就是没有名字的函数，用lambda这个关键字来定义

# lambda后面接一个参数x，然后用冒号分割，定义一个函数体

lambda x: x + 1

# 可以通过括号括起来，把参数放在后面的括号里
print((lambda x: x + 1)(3)) # 4

'''
匿名函数的特点：
1.用Lambda定义
2.参数列表不需要括号
3.冒号不是用来开启新的语句块
4.最后一个表达式没有return语句，最后一个表达式的值就是返回值

直接用括号括起来表示这里有一个匿名函数，第二对括号表示我要传参数进来了。
'''





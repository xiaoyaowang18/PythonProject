# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 2.返回值和打印值.py
@time: 2020/12/28 23:32
"""


def fn():
    pass


ret = fn()  # 返回值

print(ret)  # 打印值

'''
返回值和打印值的区别：
返回值是通过赋值符号'='进行传递值的，比如ret = add(1,2)
但是打印值只是能够在屏幕上看到输出，他并不是一个返回值，所以当用一个变量想去接住这个函数时，其实返回值是None，因为没有return，只是print

所以当函数没有return的时候，隐式的返回了一个None。
'''



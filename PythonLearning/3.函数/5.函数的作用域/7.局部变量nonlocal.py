# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 14:34
# @Author  : wanghc
# @File    : 7.局部变量nonlocal.py
# @Software: PyCharm

def counter():
    x = 0

    def inc():
        nonlocal x
        x += 1
        return x

    return inc


f = counter()
print(f()) # 1

'''
nonlocal关键字用于标记一个变量由他的上级作用域定义，通过nonlocal标记的变量可读可写

换句话说：为什么上级作用域对下级作用域只读可见？
因为赋值即定义

如果上级作用域没有定义x这个变量，就会抛出语法错误
'''




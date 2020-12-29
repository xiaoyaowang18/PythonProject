# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 10:42
# @Author  : wanghc
# @File    : 2.全局作用域.py
# @Software: PyCharm

x = 1


def inc():
    x += 1


# inc()   # UnboundLocalError: local variable 'x' referenced before assignment   局部变量x在引用前需要赋值

'''
发现调用inc函数的时候报错了，说是本地变量x没有被事先声明

这就是作用域，x在函数的外部被定义，因此x也被称为全局变量，在内部，函数是看不到x的。

函数内部是一个局部作用域，不能直接使用全局作用域的变量x

'''

def fn():
    print(x)

fn()

'''
调用fn函数，发现他能输出x的值。这是为啥？

因为每个程序都有一个全局作用域，相对于全局作用域我们就有一个局部作用域

局部作用域会随着我们层次的变深，会有多个局部作用域
'''





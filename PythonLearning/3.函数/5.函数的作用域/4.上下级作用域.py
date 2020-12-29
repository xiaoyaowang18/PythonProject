# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 11:05
# @Author  : wanghc
# @File    : 4.上下级作用域.py
# @Software: PyCharm


def fn():
    xx = 1
    print(xx)

    def inner():
        print(xx)

    inner()


fn()  # 1 1

'''
打印了2次，说明下级作用域可见上级作用域的变量。
'''


def fn2():
    xx = 1
    print(xx)

    def inner():
        xx = 2

    inner()
    print(xx)


fn2()   # 1  1

'''
发现还是1 1,不是对xx重新赋值了吗？为什么没有生效？
因为上级作用域对下级作用域是只读可见的，read-only

在python中赋值即定义，在下级作用域中，xx=2 重新定义了xx，看一下id就清楚了。
'''

def fn3():
    xx = 1
    print(id(xx))  # 140707875843840

    def inner():
        xx = 2
        print(id(xx)) # 140707875843872

    inner()
    print(id(xx))   # 140707875843840

fn3()


'''
不同作用域的变量不可见，但是下级作用域可以对上级作用域的变量只读可见
'''

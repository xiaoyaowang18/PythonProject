# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 14:07
# @Author  : wanghc
# @File    : 6.闭包函数.py
# @Software: PyCharm


def counter():
    x = 0

    def inc():
        global x
        x += 1
        return x

    return inc


f = counter()
# print(f())  # NameError: name 'x' is not defined  会提示x没有定义


def count2():
    c = [0]
    print(id(c))

    def inc():
        c[0] += 1
        print(id(c))
        return c[0]

    return inc


c = count2()
print(c())

'''
里面inc函数是一个下级作用域，所以对C这个列表是可见的。
在inc函数中改变了c本身的元素，并没有对c进行重新赋值,可以看到c的id打印出来是一致的。

这种形式称为闭包，函数已经结束，但是函数内部部分变量的引用还存在。
理论上这个c已经没有了,因为counter已经结束了，但是可以通过inc继续访问，这种就称为闭包。
'''

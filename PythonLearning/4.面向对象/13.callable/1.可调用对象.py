# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 22:47
# @Author  : wanghc
# @File    : 1.可调用对象.py
# @Software: PyCharm

'''
所谓的callable对象就是：可以通过小括号的方式调用的对象
'''


def fn():
    pass


print(fn.__class__)  # <class 'function'>

'''
所有函数都是function的实例
'''


class Fn:
    def __call__(self):
        print('{} called'.format(self))


f = Fn()
print(f())

'''
一个对象只要实现了__call__方法，就可以通过小括号来调用了，这一类对象叫可调用对象。
'''
# 可以通过callable判断是否可调用
callable(f)
callable(fn)
callable(lambda x: x)


class Addr:
    def __call__(self, x, y):
        return x + y


print(Addr()(3, 5))  # Addr()表示实例化一个对象



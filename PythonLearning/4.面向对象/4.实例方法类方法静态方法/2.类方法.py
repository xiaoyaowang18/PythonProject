# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 14:40
# @Author  : wanghc
# @File    : 2.类方法.py
# @Software: PyCharm


class A:
    def print(self):
        print('instance method')

    @classmethod
    def class_print(cls):
        print(id(cls))
        print('class method')


A.class_print()

print(id(A))  # 打印的id和class_print方法中的打印的id一致。

'''
说明当一个方法被classmethod装饰的时候，第一个参数会变成类本身，这样的方法叫做类方法。
'''

a = A()
a.class_print()  # 类方法可以被实例使用，并且被实例使用时，传入的第一个参数还是类

print(id(a))  # 打印的id和class_print方法中的打印的id不一致。

'''
类方法有什么用呢？

不需要实例化就可以执行了。
'''

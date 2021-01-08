# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 17:39
# @Author  : wanghc
# @File    : 3.变量super.py
# @Software: PyCharm

class Base:
    NAME = 'BASE'

    def __init__(self, ):
        self.a = 3


class Sub(Base):
    NAME = 'SUB'

    def __init__(self):
        self.a = 5

    def print(self):
        print(self.a)
        # 想要获取父类的实例变量
        # print(super().a)
        print(self.NAME)
        print(super().NAME)  # 可以获取类变量
        print(Base.NAME)  #


# Sub().print()  # AttributeError: 'super' object has no attribute 'a'  抛出异常，说super对象没有a
'''
想要获取父类的实例变量，实例变量需要有一个实例，这一个sub本身就不是一个实例是一个类，所以这是个伪命题
'''

Sub().print()

'''
结论：super对象只能获取类的属性
'''

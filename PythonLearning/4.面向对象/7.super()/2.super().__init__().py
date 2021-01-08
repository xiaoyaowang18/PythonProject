# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 17:00
# @Author  : wanghc
# @File    : 2.super().__init__().py
# @Software: PyCharm

class Base:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.__c = 5

    def sum(self):
        return self.a + self.b


class Sub(Base):
    def __init__(self, a, b):
        super.__init__(a, b)

    def foo(self):
        print(super().__c)


# super并不影响我们对私有属性的保护
# Sub().foo()  # super' object has no attribute '_Sub__c'

'''
super(Sub,self)
第一个参数指定调用谁的直接父类
第二个参数指定当调用时，传递什么作为方法的第一个参数


super(Sub,self)就是为了调用Sub的父类Base
'''

sub = Sub(1, 2)

print(sub.sum())

'''
当父类含有一个带参数的初始化方法时，子类在继承的时候一定要有一个初始化方法，并且在初始化方法中调整父类的初始化方法。
'''
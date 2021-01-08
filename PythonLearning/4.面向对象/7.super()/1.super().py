# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 15:47
# @Author  : wanghc
# @File    : 1.super().py
# @Software: PyCharm

'''
继承的重头戏
'''


class Base:
    def print(self):
        print('Base.print')

    @classmethod
    def cls_print(cls):
        print('Base.cls_print')


class Sub(Base):
    def print(self):
        print('Sub.print')

    @classmethod
    def cls_print(cls):
        print('Sub.cls_print')

    # 如果想调用父类的方法，可以用super()
    def foo(self):
        super().print()

    @classmethod
    def cls_foo(cls):
        super(Sub, cls).cls_print()


'''
super().print()  不带参数相当于  super(Sub,self).print()
如果想要调用父类的方法，直接用super()后面跟点号再跟成员就可以了。

另外还知道一种对等形式，就是传入一个子类和子类的实例对象。(重要)

'''

Sub().foo()
Sub().cls_print()
Sub().cls_foo()


class SubSub(Sub):
    def foo(self):
        super(Sub, self).print()

    @classmethod
    def cls_foo(cls):
        super(Sub,cls).cls_print()


SubSub().foo()  # Base.print
SubSub().cls_foo()  #Base.cls_print

# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 15:30
# @Author  : wanghc
# @File    : 4.方法重写.py
# @Software: PyCharm

class Base:
    def print(self):
        print('Base.print')


class Sub(Base):
    def print(self):
        print('Sub.print')


sub = Sub()
sub.print()  # Sub.print

'''
打印的是sub.print

当子类和父类有同名成员的时候，子类的成员会覆盖父类的同名成员，无论是属性和方法都一样的。
这就是重写。
'''


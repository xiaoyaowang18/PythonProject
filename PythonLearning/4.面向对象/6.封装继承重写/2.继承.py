# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 10:45
# @Author  : wanghc
# @File    : 2.继承.py
# @Software: PyCharm


class Base:
    def base_print(self):
        print('base')


'''
继承最基本的写法：在类名后面加括号，括号中是继承列表
'''


class A(Base):
    def a_print(self):
        print('A')


'''
继承的好处：
1.括号里我们称为父类或基类或超类
2.这里Base就是我们的父类，A就是我们的子类
3.继承可以获得父类的属性和方法，意味着我们的代码能够被重用
'''

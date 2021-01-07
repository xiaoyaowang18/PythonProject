# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 14:49
# @Author  : wanghc
# @File    : 3.静态方法.py
# @Software: PyCharm


'''
还有一个装饰器叫做@staticmethod，对于第一个参数没有实质要求

静态方法：用staticmethod修饰，对参数无要求，跟着类走，借用类的命名空间，类和对象皆可调用。
'''


class A:
    def print(self):
        print('instance method')

    @classmethod
    def class_method(self):
        print('class method')

    @staticmethod
    def static_method():
        print('static method')


a = A()
a.static_method()


'''
当一个方法被staticmethod装饰的时候，不会自动传递第一个参数，这样的方法叫做静态方法
'''

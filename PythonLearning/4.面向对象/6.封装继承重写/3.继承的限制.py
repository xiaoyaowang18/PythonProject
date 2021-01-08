# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 11:03
# @Author  : wanghc
# @File    : 3.继承的限制.py
# @Software: PyCharm

# 先定义一个基类
class Base:
    PUBLIC_CLASS_VAR = 'PUBLIC_CLASS_VAR'
    __PRIVATE_CLASS_VAR = 'PRIVATE_CLASS_VAR'

    def __init__(self):
        self.public_instance_var = 'pulbic_instance_var'
        self.__private_instance_var = 'private_instance_var'

    @classmethod
    def public_class_method(cls):
        return 'public_class_method'

    @classmethod
    def __private_class_method(cls):
        return 'private_class_method'

    @staticmethod
    def public_static_method():
        return 'public_static_method'

    @staticmethod
    def __private_static_method():
        return 'private_static_method'

    def public_instance_method(self):
        return 'public_class_method'

    def __private_instance_method(self):
        return 'private_class_method'


'''
继承Base类，访问公有的类属性，发现是可以的
'''


class Sub(Base):
    def print(self):
        print(self.PUBLIC_CLASS_VAR)


sub = Sub()
sub.print()  # PUBLIC_CLASS_VAR

'''
继承Base类，访问私有的类属性，发现是不可以的
'''


class Sub2(Base):
    def print(self):
        print(self.__PRIVATE_CLASS_VAR)


sub = Sub2()
# sub.print()  # Sub2' object has no attribute '_Sub2__PRIVATE_CLASS_VAR'


'''
公有的实例属性可以访问，但是私有的实例属性不可以访问
'''


class Sub3(Base):
    def print(self):
        print(self.public_instance_var)
        print(self.__private_instance_var)


sub3 = Sub3()
# sub.print()

'''
公有的类方法，静态方法，实例方法可以访问、
私有的类方法，静态方法，实例方法不可以访问
'''


class Sub4(Base):
    def print(self):
        print(self.public_class_method())
        print(self.public_static_method())
        print(self.public_instance_method())
        print(self.__private__class_method())
        print(self.__private_static_method())
        print(self.__private_instance_method())


sub4 = Sub4()

'''
总结：
1.凡是公有的都能继承
2.凡是私有的都不能继承
3.原来是什么，继承过来还是什么
'''

print(sub3.__dict__)  # {'public_instance_var': 'pulbic_instance_var', '_Base__private_instance_var': 'private_instance_var'}
'''
发现私有变量，在前面加上了一个 下划线+类名称
所以我们继承不到父类的私有变量。
'''

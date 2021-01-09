# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 1.多继承.py
@time: 2021/1/9 11:12
"""

'''
python是允许多继承的，事实上，所有的python类都会继承我们的Object类
'''


class A:
    pass


class A(object):
    pass


# 上面这2个类是完全等价的。 通常我们会省略object，并且去掉括号。

a = A()
print(dir(a))


class Base:
    pass


class Sub(Base):
    pass


# Sub类其实相当于是这样的，相当于多继承。
class Sub(Base, object):
    pass


'''
在继承列表中存在多个类时，就表示多继承。
多继承会把继承列表里的所有公有成员都继承过来。

那么当公有成员重名了会怎么办？  比如Base和Base2中都有一个Print方法，会调用谁的？
'''


class A:
    def method(self):
        print('A method')


class B:
    def method(self):
        print('B method')


class C(A, B):
    pass


class D(A, B):
    pass


c = C()
c.method()  # A method

d = D()
d.method()  # B method


# 发现谁在前就打印谁，这种结论对不？

class E(A):
    def method(self):
        print('E method')


# class F(A, E):
# pass

class G(E, A):
    pass


# f = F()
# f.method()  #  报错： order (MRO) for bases A, E

g = G()
g.method()  # E method  调用没问题    为什么呢？

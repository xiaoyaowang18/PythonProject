# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 2.mro.py
@time: 2021/1/9 11:28
"""


class A:
    def method(self):
        print('A method')


class B:
    def method(self):
        print('B method')


class E(A):
    def method(self):
        print('E method')


class G(E, A):
    pass


'''
MRO:方法查找顺序

需要满足几个特性：
1.本地优先：自己定义或重写的方法优先，按照继承列表，从左到右查找
2.单调性：所有子类，也要满足查找顺序（G继承E和A，既要满足E的MRO还要满足A的MRO）
'''

#  每个类都有一个mro属性。  可以看到既满足了本地优先，又满足了单调性
print(A.__mro__)  # (<class '__main__.A'>, <class 'object'>)
print(E.__mro__)  # (<class '__main__.E'>, <class '__main__.A'>, <class 'object'>)
print(G.__mro__)  # (<class '__main__.G'>, <class '__main__.E'>, <class '__main__.A'>, <class 'object'>)

'''
python通过C3算法来确定是否满足mro的两个原则

class B(A1,A2,...,An)  ->  [B] + merge(mro(A1),mro(A2),mro(A3),....,mro(An)),[A1,A2,...An,O]
merge算法的步骤：
1.遍历列表
2.看第一个列表的首元素
A.他在其他列表中也是首元素
B.他在其他列表不存在
3.如果满足以上2种情况，移除，合并到MRO
4.如果不满足，抛出异常。

mro(G) -> [G] + merge(mro(E),mro(A),[E,A,O])

展开后： 
[G] + merge([E,A,O],[A,O],[E,A,O])

Merge过程：首先去除第一个列表的首元素E，在其他列表中不存在，提取出来
[G,E] + merge([A,O],[A,O],[A,O])
下一步提取A
[G,E,A] + merge([O],[O],[O])
[G,E,A,O]

看一下F为什么不行
mro(G) -> [G] + merge(mro(A),mro(E),[A,E,O])
[F] + merge([A,O],[E,A,O],[A,E,O])
发现不满足首元素条件，抛出异常


最后不建议用多继承，因为容易混淆当继承较深，类很多的时候。
'''

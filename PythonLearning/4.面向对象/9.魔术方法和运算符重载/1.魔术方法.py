# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 22:28
# @Author  : wanghc
# @File    : 1.魔术方法.py
# @Software: PyCharm

class A:
    '''hhh'''
    pass


print(dir(A))

'''通过dir方法可以得到所有公有成员。双下划线开始，双下划线结束。有些是属性，有些是方法
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
'''
print(A.__name__)  # 类的名字   A
print(A.__module__)  # 模块的名字  __main__
print(A.__doc__)  # 文档  hhh
print(A.__class__)  # <class 'type'>

a = A()
a.xxx = 3
print(a.__dict__)  # dict针对实例的特有属性，实例的所有属性都保存在__dict__里。
print(a.__dir__())  # a.__dir__()会得到所有成员，包括方法和属性。dir函数就是调用的这个，只不过他做了个排序


'''
成员分类：
创建/销毁（__init__函数）
运算符重载
hash
bool
可视化
反射
上下文管理
大小
描述器
杂项
'''

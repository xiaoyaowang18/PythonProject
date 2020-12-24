# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 1.定义.py
@time: 2020/12/24 21:55
"""

'''
字典是一种key-value结构
'''

# 空字典是通过一对空的花括号定义的
d = {}
print(type(d))  # <class 'dict'>

# 还有几种定义的方法

# 1.直接使用dict()来定义，如果要传值就通过k=v的方式来传递。
d1 = dict(name='whc', age=18)
print(d1)

# 2.直接用花括号括起来
d2 = {'a': 1, 'b': 2}
print(d2)

# 3.要求：可迭代对象的元素必须是一个二元组，二元组的第0个元素是字典的key，第一个元素是字典的value
d3 = dict([('a', 1), ('b', 2)])
print(d3)

# 4.传入可迭代对象为key，值为None
d4 = dict.fromkeys(range(5))
print(d4)

# 5.传入可迭代对象为key，值为abc
d5 = dict.fromkeys(range(5), 'abc')
print(d5)

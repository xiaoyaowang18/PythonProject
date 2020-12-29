# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 4.应用.py
@time: 2020/12/30 0:23
"""

# 匿名函数在高阶函数中用的比较多

# 4.1 sorted
# print(help(sorted))
'''
sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
    
里面传一个可迭代对象，key function默认为None,用来定制排序顺序，reverse表示是否翻转
'''
L = [1, 4, 5, 2, 6, 9, 7]
y = sorted(L, key=lambda x: x)
print(y)

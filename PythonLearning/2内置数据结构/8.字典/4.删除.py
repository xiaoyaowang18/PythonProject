# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 4.删除.py
@time: 2020/12/24 22:49
"""

d = dict(
    name='whc',
    age=18,
    weight=60,
    height=174
)

# 1. dict.pop
# print(help(dict.pop))
'''
pop(...)
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    If key is not found, d is returned if given, otherwise KeyError is raised

和List不一样，pop需要传入一个指定的key，这个key就是字典中的键，它会返回这个key的value。
如果key不存在，如果传入了第二个参数d，那么不存在的时候就返回给你d，所以d就是默认值default。
'''

print(d.pop('name'))  # 返回whc   所以pop方法是用来删除字典的一个键值对，并返回其value

# print(d.pop('address'))  # 当key不存在时，抛出keyerror

print(d.pop('address', '哈哈'))  # 当删除不存在的key时，并且指定了默认值，不会抛出keyerror，会返回这个默认值。

# 2.dict.popitem
# help(d.popitem)
'''
    Remove and return a (key, value) pair as a 2-tuple.
    Pairs are returned in LIFO (last-in, first-out) order.
    Raises KeyError if the dict is empty.
返回一个k-v对的二元组，如果字典为空的话，就会返回Keyerror。
'''
print(d.popitem())

# 3. dict.clear
# 清空一个字典
d.clear()
print(d)

# 4.del
# del语句删除一个引用，是一个键的引用，相当于dict.pop(k)
d2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
del d2['a']
print(d2)


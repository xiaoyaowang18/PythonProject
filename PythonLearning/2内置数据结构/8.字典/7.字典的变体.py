# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 7.字典的变体.py
@time: 2020/12/24 23:30
"""

# 1.默认字典
from collections import defaultdict

# print(help(defaultdict))
'''
|  defaultdict(default_factory[, ...]) --> dict with default factory
 |  
 |  The default factory is called without arguments to produce
     |  a new value when a key is not present, in __getitem__ only.
     |  A defaultdict compares equal to a dict with the same items.
     |  All remaining arguments are treated the same as if they were
 |  passed to the dict constructor, including keyword arguments.

defaultdict初始化的时候，需要传入一个函数，这个函数也叫工厂函数
当我们使用一个下标访问一个key的时候，如果这个key不存在，defaultdict会自动调用初始化时传入的函数，生成一个对象作为这个key的value
'''
d = {}
for k in range(10):
    for v in range(10):
        if k not in d.keys():
            d[k] = []
        d[k].append(v)
print(d)

# 不需要再去判断有没有值了，因为没有值的时候，他会去找defaultdict初始化时传入的那个工厂函数
d2 = defaultdict(list)  # 传入list,初始化的时候把它初始化成了一个空列表
for k in range(10):
    for v in range(10):
        d2[k].append(v)
print(d2)

# 2.有序字典
# 使用OrderedDict这个类之后，我们的字典变的有序输出了。
# 从python3.6之后，字典开始变的有序了，官方做了处理。但是字典本身的数据结构一定是无序的
from collections import OrderedDict

d = OrderedDict()
d[0] = 3
d[3] = 4
d[1] = 5
print(d)
for k, v in d.items():
    print(k, '=>', v)

# Q:什么时候需要用有序字典？   A: 既是k-v对，又需要顺序的时候

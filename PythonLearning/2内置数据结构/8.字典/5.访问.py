# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 5.访问.py
@time: 2020/12/24 23:13
"""

# 1.单个元素的访问
# 当访问的key不存在时会抛出keyerror
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d['a'])

# 2.get
print(d.get('b'))  # 返回2
print(d.get('e'))  # 返回None. get访问不存在key时返回None。事实上返回的是一个默认值，只不过这个默认值为None。

'''
访问单个元素，要么用下标，要么用get方法。
'''

# 3.字典的遍历
'''
直接用for in 遍历字典，遍历的是字典的key
d.values() 返回一个可迭代对象，元素是字典的所有value
d.items() 用的最多，返回一个可迭代对象，元素是字典的所有(k,v)对
'''
for k, v in d.items():
    print(k ,',' ,v)

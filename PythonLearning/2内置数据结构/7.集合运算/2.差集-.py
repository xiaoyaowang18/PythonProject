# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 23:11
# @Author  : wanghc
# @File    : 2.差集-.py
# @Software: PyCharm

'''
记A、B是两个集合，所有属于A且不属于B的元素构成的集合，叫做集合A减集合B
'''

s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1.difference(s2))  # {1}
print(s2.difference(s1))  # {4}

# update版本
print(s1)  # {1, 2, 3}
# s1.difference_update(s2)
# print(s1)  # 1

# 重载运算符  set重载了运算符，执行了差集运算，相当于s1.difference(s2)
print(s1 - s2)  # {1}
print(s2 - s1)  # {4}


# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 23:21
# @Author  : wanghc
# @File    : 3.对称差集^.py
# @Software: PyCharm


'''
对称差集：集合A与集合B中所有不属于A∩B元素的集合

A、B交集的补集
'''

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.symmetric_difference(s2))  # {1,4}
print(s2.symmetric_difference(s1))  # {1,4}

# update版本
# s1.symmetric_difference_update(s2)
# print(s1)  # # {1,4} 原地修改，返回None

# 对称差集重载了异或运算符
print(s1 ^ s2)

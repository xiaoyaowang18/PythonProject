# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 21:27
# @Author  : wanghc
# @File    : 1.交集&.py
# @Software: PyCharm


'''
集合论：
A,B是两个集合，由所有属于集合A且属于集合B的元素所组成的集合，叫做集合A和集合B的交集（intersection） 记作A∩B

两个集合的相同部分
'''

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1.intersection(s2)  # 原地不修改，有返回值
print(s1)  # {1, 2, 3}
print(s2)  # {2, 3, 4}
print(s3)  # {2, 3}

s1.intersection_update(s2) # 原地修改，返回None
print(s1)  # {2, 3}
print(s2)  # {2, 3, 4}

# python中，set 重载了按位与运算符为求交集的运算 与intersection效果一样
print(s1 & s2)

# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 23:31
# @Author  : wanghc
# @File    : 4.并集.py
# @Software: PyCharm

'''
并集：
若A、B是集合，A和B并集是所有A的元素和所有B的元素，没有其他元素的集合。
'''

s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1.union(s2))  # {1, 2, 3, 4}

# 并集的update版本就是update,不是union_update
s1.update(s2)
print(s1)  # {1, 2, 3, 4}

# 并集的重载运算符不是+，是 |   set重载了按位或运算符，用于并集计算
print(s1 | s2)


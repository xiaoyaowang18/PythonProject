# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 11:43
# @Author  : wanghc
# @File    : 求质数.py
# @Software: PyCharm

# 质数：在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。

lst = []

for x in range(1, 1000):
    for y in range(1, 1000):
        if x % y == 0 and (y > 1 and x != y):
            break
    else:
        lst.append(x)

print(lst)

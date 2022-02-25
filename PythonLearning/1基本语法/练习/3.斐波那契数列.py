# -*- coding: utf-8 -*-
# @Time    : 2020/1/14 22:21
# @Author  : wanghc
# @File    : 3.斐波那契数列.py
# @Software: PyCharm

# 以兔子繁殖为例子引入，又称兔子数列

# 1 1 2 3 5 8 13 21 34 ...

# F(0) = 1 F(1) = 1    n> 1: F(n) = F(n-1) + F(n-2)

x = 0
y = 0
for i in range(0, 10):
    if i == 0:
        y = 1
    elif i == 1:
        x = 1
        y = 1
    else:
        tmp = y
        y = x + y
        x = tmp
print(y)
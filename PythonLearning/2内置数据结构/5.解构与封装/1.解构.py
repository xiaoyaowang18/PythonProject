# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 16:36
# @Author  : wanghc
# @File    : 1.解构.py
# @Software: PyCharm

x = 1
y = 2
tmp = x
x = y
y = tmp

# 以上交换x,y值的方法，在python里有很巧妙的写法（解构）
x, y = y, x

'''
解构：顾名思义，把一个整体拆分成多个小个体
'''
lst = [1, 2]
first = lst[0]
second = lst[1]
print(first, second)

# 上述是传统的做法，在python中可以这么做
'''
这个过程称为解构。
按照元素顺序，把线性解构的元素赋值给变量
'''
first, second = lst
print(first, second)

# -*- coding: utf-8 -*-
# @Time    : 2020/12/30 17:38
# @Author  : wanghc
# @File    : 2.高阶函数的作用.py
# @Software: PyCharm

# 函数作为参数，使用lambda匿名函数

def sort(it, cmp=lambda a, b: a < b):
    ret = []
    for x in it:
        for i, e in enumerate(ret):
            if cmp(x, e):
                ret.insert(i, x)
                break
        else:
            ret.append(x)
    return ret


print(sort([3, 2, 1, 7, 4]))

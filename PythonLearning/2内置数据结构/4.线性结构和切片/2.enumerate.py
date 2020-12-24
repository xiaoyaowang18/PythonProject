# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 22:30
# @Author  : wanghc
# @File    : 2.enumerate.py
# @Software: PyCharm


'''
enumerate  返回一个可迭代对象
同时获取索引和value的时候需要用到这个函数
'''
# 实现一个enumerate函数
def new_enumerate(iterator):
    ret = []
    i = 0
    for v in iterator:
        ret.append((i,v))
        i+=1
    return ret

print(new_enumerate([1,2,3]))  # [(0, 1), (1, 2), (2, 3)]


print(list(enumerate([1,2,3]))) # [(0, 1), (1, 2), (2, 3)]


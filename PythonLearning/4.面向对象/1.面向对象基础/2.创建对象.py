# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 16:29
# @Author  : wanghc
# @File    : 2.创建对象.py
# @Software: PyCharm


class D:
    def __init__(self):
        print(id(self))

'''
验证一下self和类的关系
'''

d = D()   # 初始化类的时候，执行init函数，打印了self的id

print(id(d)) # 发现d这个对象的id和self的id一致。

# 说明self就是我们的类

'''

那么，是先有self，还是先有init呢？

发现init函数是没有return的，那么应该是先有self

init函数用来初始化我们的类

'''
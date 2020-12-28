# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 22:00
# @Author  : wanghc
# @File    : 1.函数的基础.py
# @Software: PyCharm


'''
1、什么叫做线性结构？
目前已经学了 列表、元组、字符串、byte、bytearray
有什么共同特点呢？都是顺序存储，顺序访问的，都是可迭代对象，都可以通过索引访问。
这样一类的结构我们称为：线性结构。

线性结构特点：
可迭代
可以用len方法获取长度
可以使用下标操作符通过索引访问
可以切片
'''
for i in [1,2,3]:
    print(i)

for i in (1,2,3):
    print(i)

for i in 'i love you':
    print(i)


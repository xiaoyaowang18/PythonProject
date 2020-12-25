# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 15:46
# @Author  : wanghc
# @File    : 2.迭代器.py
# @Software: PyCharm

'''
7种数据结构：
    list
    tuple
    str
    bytes
    byte_array
    dict
    set

有__next__方法的可迭代对象叫迭代器。

上述7种数据结构都不是迭代器，但是可迭代对象可以转换为迭代器
iter函数可以把一个可迭代对象转换为迭代器。

为什么要转换？
因为迭代器可以使用next()，next函数可以从迭代器中取出下一个元素。

可迭代对象并不是迭代器，必须要有next方法才称为迭代器。
迭代器既要有next方法，又要有iter方法。
'''

ddq = iter(range(10))

print(type(ddq))  # <class 'range_iterator'>

# 迭代器会保存一个指针，指向可迭代元素的当前元素
# 当前指针指向it的头，当调用过it的时候，就会返回当前元素，并且把指针指向下一个元素

print(next(ddq)) # 0
print(next(ddq)) # 1

# 当没有下一个元素的时候，会抛出StopIteration异常。


# for .. in ..
'''
实现原理：
1、首先调用iter方法，将可迭代对象转化为迭代器
2、不断调用next方法
3、直到抛出StopIteration异常，抛出异常后for循环做了异常处理，直接退出，而不是让用户每次循环后都看到这个错误
'''

ddq2 = iter(range(10))

def forin():
    while True:
        try:
            print(next(ddq2))
        except StopIteration:
            return

forin()












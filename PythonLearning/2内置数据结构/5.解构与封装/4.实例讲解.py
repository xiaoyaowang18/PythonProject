# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 18:13
# @Author  : wanghc
# @File    : 4.实例讲解.py
# @Software: PyCharm


list = [1, 2]

head, *mid, last = list

# 如果用星号变量去承接的时候，如果其他元素正好分完所有元素，那么星号元素就是空列表
print(head)  # 1
print(mid)  # []
print(last)  # 2

'''
问题1.为什么多个星号不行？
因为python不知道分发给谁多少个，m1和m2都是星号，到底分谁几个没办法判断。
'''
# head,*m1,*m2,last = list

'''
问题2.为什么左边只有一个星星不行？
'''
# *m = list 如果可以，其实就是 m = list.copy() 也就没必要星号解构了。
tp = (1, 2, 3, 4)
t1, *t2 = tp
# 无论右边是什么类型，带星号的类型都是列表。
print(t2)  # [2, 3, 4]

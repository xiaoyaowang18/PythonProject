# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 23:22
# @Author  : wanghc
# @File    : 6.其他操作.py
# @Software: PyCharm

l = [1, 2, 3, 4, 5]

# 6.1 求list的长度
print(len(l))

# 6.2 翻转列表
l.reverse()
print(l)

# 6.3 排序
l.sort()
print(l)

# 逆序排序
l.sort(reverse=True)
print(l)

# 6.4 列表拷贝
list1 = [1,2,3,4,5]
list2 = list1
list2[0] = 5
print(list2)  # [5, 2, 3, 4, 5]
print(list1)  # [5, 2, 3, 4, 5]
# l2做修改，l也被修改了
'''
赋值操作是引用传递，也叫浅复制，浅拷贝
浅拷贝会产生引用关联（引用到同一个内存地址），导致不希望被修改的值被修改了。
'''

# 6.4.1 影子拷贝
# help(list.copy)
'''
copy(...)
    L.copy() -> list -- a shallow copy of L
'''
list3 = [1,2,3]
list4 = list3.copy()    # list4 copy了一份list3 ,  修改list4的元素，list3没有被修改。
list4[0] = 3
print(list3) # [1,2,3]
print(list4) # [3,2,3]

# 6.4.2 深拷贝
list5 = [1,[1,2,3],2,3]
list6 = list5.copy()
list6[1][1] = 3
print(list6) # [1, [1, 3, 3], 2, 3]
print(list5) # [1, [1, 3, 3], 2, 3]
'''
发现 list6改变后，list5还是跟着变了
'''
# 还原浅拷贝
def copy(list):
    tmp = []
    for i in list:
        tmp.append(i)
    return tmp
'''
所以内嵌在里面的列表还是相当于一个浅复制。
赋值操作，对于可变对象来说是引用传递，对于不可变对象来说是值传递。
'''

# 要使用深拷贝，需要引入copy模块，使用deepcopy
from copy import deepcopy
list7 = [1,['a'],2]
list8 = deepcopy(list7)
list8[1][0] = 'b'
print(list8)  #[1, ['b'], 2]
print(list7)  #[1, ['a'], 2]
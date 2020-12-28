# -*- coding: utf-8 -*-
# @Time    : 2020/1/20 18:24
# @Author  : wanghc
# @File    : 3.下标操作.py
# @Software: PyCharm

'''
下标访问就是Python的神奇之处了，对于字符串来说，其他语言都是打包一个整体，但是python的字符串就像列表一样，可以使用下标来访问
'''

s = '人人都是\npythonista'

print(s[4])

# 1.无法修改字符串的某个元素
# s[1] = 'a'  # TypeError: 'str' object does not support item assignment
'''
因为无法赋值，所以字符串是不可变的
目前只有list是可变的，其他都是不可变的
字符串是可迭代对象
'''
for i in s:
    print(i)

# 2.使用list()方法快速将字符串转化为列表，就等于将字符串的每个元素拆开来，append到list里。
h = list(s)
print(h)
# 相当于如下操作：
lst = []
for c in s:
    lst.append(c)

# 3.通过s.count()可以对字符串中的某个字符进行计算,相当于下面的函数
print(s.count('都'))


def count_s(lst,value):
    count = 0
    for i in s:
        if i == value:
            count += 1
    return count


print(count_s(s,'人'))

# 4.在字符串中也可以用index搜索列表中某个字符或者字符串在列表的第几个位置
print(s.index('都'))


def index_s(lst,value,start=0,end=-1):
    p = 0
    for i in lst[start:end]:
        if i == value:
            return p
        p += 1

print(index_s(s,'人'))

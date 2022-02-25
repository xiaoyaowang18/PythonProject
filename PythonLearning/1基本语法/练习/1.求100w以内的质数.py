# -*- coding: utf-8 -*-
# @Time    : 2020/1/14 7:15
# @Author  : wanghc
# @File    : 1.求100w以内的质数.py
# @Software: PyCharm

# 质数：整数在大于1的自然数中，除了1和此整数以外，没法被其他自然数整除的数。

'''x = 10
if x != 1:
    for i in range(2, x):
        if x % i == 0:  # 如果遇到整除，跳出循环
            break
    else:
        print(x)  # 提前退出  则不会执行else语句'''

# 加一个临时变量 c ，看for循环执行了几次
'''x = 10
if x!=1:
    c = 0
    for i in range(2,x):
        c += 1
        if x % i == 0:
            break
    print(c)'''

'''x = 11
if x!=1:
    c= 0
    for i in range(2,x):  #  i = [2,10]
        c += 1
        if x%i == 0:
            break
    if c == x-2:
        print(x)'''

c = 0
for x in range(2, 100):
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        c += 1  # 当for循环没有提前退出(说明x这个数是质数)，c +1
print(c)
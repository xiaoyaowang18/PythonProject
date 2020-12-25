# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 14:41
# @Author  : wanghc
# @File    : 斐波那契数列.py
# @Software: PyCharm

'''
斐波那契数列（Fibonacci sequence），又称黄金分割数列、
因数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”，
指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
在数学上，斐波那契数列以如下被以递推的方法定义：F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 2，n ∈ N*）
'''

lst = []
a = 0
b = 1


for x in range(10):
    if x == 0 or x == 1:
        lst.append(x)
    else:
        tmp = a
        a = b
        b = b + tmp
        lst.append(b)

print(lst)



def fbnqsl(n):
    if n == 0 or n == 1:
        return n
    else:
        return fbnqsl(n - 1) + fbnqsl(n - 2)



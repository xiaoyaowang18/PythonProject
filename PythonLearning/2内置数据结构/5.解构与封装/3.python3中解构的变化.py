# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 17:20
# @Author  : wanghc
# @File    : 3.python3中解构的变化.py
# @Software: PyCharm

# 变体1
# head第一个元素 mid中间所有元素 tail最后一个元素
lst = list(range(10))
head,*mid,tail = lst
print(head)
print(mid)
print(tail)

# 变体2
# 加星号的tail是除了第一个外的所有元素
head,*tail = lst
print(head)
print(tail)

# 变体3
# 加星号的head是除了最后一个外的所有元素
*head,tail = lst
print(head)
print(tail)

# 变体4
# 左边只有一个带*的变量是不行的
# *lst2 = lst

# 变体5
# 左边有2个或2个以上加星号的是不行的 （一个层次中）
# head,*second,*third,fourth = lst  SyntaxError: two starred expressions in assignment

# 变体6
# 左边再加上其他变量
head,second,*third,last = lst
print(third)

# 变体7
# 左边元素超过右边元素个数的时候是不允许的

# 变体8
# 当左边变量数小于右边变量数，且左边没有加星号的变量，是不允许的。

'''
总结：
元素按照顺序赋值给变量
变量和元素必须匹配
加星号变量，可以接受任意个数的元素
加星号的变量不能单独出现
'''
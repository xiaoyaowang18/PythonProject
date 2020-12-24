# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 22:18
# @Author  : wanghc
# @File    : 7.拓展.py
# @Software: PyCharm

# 1.异或

# 5 xor 2 = 7

'''
5: 0101 二进制
2：0010
   0111 异或后
= 7
'''

# 2.异或的使用场景
# 交换2个整数的值而不必使用第三个参数,也可以用解构来实现
a = 9
b = 11

a = a ^ b
b = b ^ a
a = a ^ b

print(a)
print(b)



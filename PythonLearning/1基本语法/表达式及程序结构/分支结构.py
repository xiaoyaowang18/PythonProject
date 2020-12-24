# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 22:16
# @Author  : wanghc
# @File    : 分支结构.py
# @Software: PyCharm

# 2.表达式 & 语句
'''
表达式： 常量/变量和运算符一起构成，表达式有返回值
语句： 关键字和表达式一起组成语句，语句没有返回值
'''

# 3.顺序结构
i = 3
print(i)
i += 5
print(i)

# 4.分支结构
# 4.1 单分支
# 单分支就是只有一个判断，当条件成立时，去做操作，然后结束，否则直接结束。
a = 5
if a < 10:
    print('a less than 10')
print(a)

# 4.2 双分支
# 当条件不成立的时候还多了一个操作，方便我们做逻辑处理
a = 15
if a < 10:
    print('a less than 10')
else:
    print('a is not less than 10')

# 4.3 嵌套
a = 15
if a < 10:
    print('a less than 10')
else:
    if a < 20:
        print('10<= a <20')
    else:
        print('a is not less than 10')

# 4.4 关键字elif
a = 25
if a < 10:
    print('a is less than 10')
elif a < 20:
    print('10<= a < 20')
else:
    print('a>=20')

'''
1.分支结构永远只有1个或者0个分支会被执行
2.分支结构中的所有条件都是互斥的
3.条件只能是bool类型或者可以隐式转换为bool类型
'''




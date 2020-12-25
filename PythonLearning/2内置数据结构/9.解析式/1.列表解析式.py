# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 10:12
# @Author  : wanghc
# @File    : 1.列表解析式.py
# @Software: PyCharm

'''
1.通用语法： [expr for e in iterator]

在这个expr表达式中我们可以用我们的元素，这样子列表解析式和我们的for循环是等价的。

优点：
    代码简洁，可读性强。
    效率比普通的迭代要高，但并不是数量级上的，只是稍微有一点
'''

a = [i * 2 for i in range(5)]
print(a)  # [0, 2, 4, 6, 8]

# 2.解析式变体
# 带if语句的列表解析

b = [i * 2 for i in range(5) if i % 2 == 0]
print(b)  # [0, 4, 8]

# 也可以是多个if的组合
c = [i * 2 for i in range(5) if i % 2 == 0 if i > 1]
print(c)  # [4, 8]

# 表达式中需要有一个或的关系，怎么做？
d = [i * 2 for i in range(6) if i > 4 or i < 2]
print(d)  # [0, 2, 10]

e = [i * 2 for i in range(6) if i > 2 and i < 5]
print(e)  # [6,8]

# 3.可以用多个for语句，相当于循环嵌套
'''
result = []
for x in range(5):
    for y in range(10):
        result.append((x,y))
'''
f = [(x, y) for x in range(5) for y in range(10)]
print(f)

# 4.什么时候该用列表解析式？
# 跟着感觉走哈哈，太复杂的逻辑就不要用了，一眼就能看出解析式的结果的话可以用


# 5.三元表达式
'''
x if cond else y 
当条件cond满足时，返回x
当条件不满足时，返回y
只能用双分支
'''
g = [x * 2 if x % 2 == 0 else x * 3 for x in range(5)]
print(g)




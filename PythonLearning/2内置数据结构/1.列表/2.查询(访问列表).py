# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 7:25
# @Author  : wanghc
# @File    : 2.查询(访问列表).py
# @Software: PyCharm

# 定义一个1-10的列表
l = list(range(1, 10))
print(l)

# 下标从0开始
print(l[0])

# 下标超出范围，抛出indexerror
# print(l[100])

# 2.1 list.index
print(l.index(4))  # 返回查找到的第一个索引
# 可以通过help()函数查看所有方法的函数签名，也就是函数说明
# help(l.index)
'''
  L.index(value, [start, [stop]]) -> integer -- return first index of value.
  Raises ValueError if the value is not present.
'''
x = l.index(3, 1, 5)  # 从1开始，到5结束，但不包括索引我5的元素，左闭右开。
print(x)


# start end参数可以为负数，但在查找的过程中还是从左到右。

# 2.1.1 list.index 函数解读

def index(lst, value, start=0, end=-1):
    # 定义一个起始位置，这里的起始位置就是start
    i = start
    # 用for循环迭代list对象
    for x in lst[start:end]:
        # 如果value是我们要找的值，当value存在，返回当前 i
        if x == value:
            return i
        # 如果不是, i + 1
        i += 1
    raise ValueError()


# 测试
x = [1, 2, 3, 4, 5]
print(x[0:3])
print(index(x, 3, 0, 3))

# 2.2 list.count
help(l.count)
'''
Help on built-in function count:

count(...) method of builtins.list instance
    L.count(value) -> integer -- return number of occurrences of value
'''


# 2.2.1 list.count函数解读
def count(lst, value):
    # 这个c是计数器，用来统计我们要查找的value再list有几个
    c = 0
    for i in lst:
        # 当元素和value相等时，c+1
        if i == value:
            c += 1
    return c


# 总结
'''
1.通过索引访问元素
2.index方法返回第一个索引
3.count方法返回元素在列表里的个数

list,count的时间复杂度是O(n)
'''

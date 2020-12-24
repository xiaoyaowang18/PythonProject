# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 22:35
# @Author  : wanghc
# @File    : 3.迭代器.py
# @Software: PyCharm


'''
先看range函数，是用来取一段范围内的数字，可能是连续的，可能不连续
range(10) range(1,10) range(1,10,2)
三个参数：
start 开始 end 结束 step 步长
'''

print(list(range(1,10,3))) # [1, 4, 7]

'''
next函数是用来迭代 可迭代对象的
next函数需要一个迭代器，而iter方法可以转化可迭代对象成为迭代器
next不能直接迭代可迭代对象
'''

list = [1,2,3]
# next(list) TypeError: 'list' object is not an iterator

it = iter(list)
#print(type(it)) # <class 'list_iterator'>

print(next(it))
print(next(it))
print(next(it))
print(next(it)) # StopIteration 元素迭代完后再迭代，会抛出StopIteration

'''
记住：可迭代对象可以通过iter函数转换为迭代器，而迭代器能被next函数迭代
迭代器作用？
举例：
当List很大时，可能100w个元素，存在内存中是很占资源的，这个时候需要惰性求值，你需要的时候我给你。
实际工作中，经常把这种List转化为迭代器，方便获取数据，降低性能消耗。
'''



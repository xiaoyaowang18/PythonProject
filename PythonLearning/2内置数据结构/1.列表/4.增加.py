# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 22:07
# @Author  : wanghc
# @File    : 4.增加.py
# @Software: PyCharm

# 4.1 list.append
# help(list.append)
'''
Help on method_descriptor:

append(...)
    L.append(object) -> None -- append object to end
'''

#  append原地修改list ,返回值是None，直接加在最后一位，追加。
l1 = [1, 2, 3]
l1.append(4)
print(l1)

'''
1.原地修改：这个方法会影响原来对象的结果。本来l1是[1,2,3],append(4)以后,l1变成[1,2,3,4],就回不去了。
2.返回值是None: None的意思是没有返回值。没有返回值，返回值就是None，返回None,返回值也是None。
'''

# 4.2 list.insert
# help(list.insert)
'''
Help on method_descriptor: 

insert(...)
    L.insert(index, object) -- insert object before index
'''

# 在第i个元素前插入
l2 = ['w', 'h', 'c']
l2.insert(-1, 'a')
print(l2)

# 当越界的时候，自动往最左或最右插入该值，并不会报错。

'''
append和insert的效率：
1.append的时间复杂度是O(1),常数时间,效率和数据的规模无关。
2.insert的时间复杂度是O(n),线性时间,效率和数据规模线性有关。
尽量使用append。
'''

# 4.3 list.extend
# help(list.extend)
'''
extend(...)
    L.extend(iterable) -> None -- extend list by appending elements from the iterable

extend 可以将任意可迭代对象追加到数据的末尾，原地修改，返回None。
extend 是把可迭代对象里的每一个值循环append到list去，而不是像append，直接把一整个对象追加到列表末尾。
'''
# list.extend 可以用在两个list想加上，这样就不用去写一个循环了
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# 4.4 list + list
list3 = [1, 2, 3, 4]
list4 = [5, 6, 7]
print(list3+list4)  # 这种方法有返回值，但是不修改List本身，返回一个新的list，list的连接操作。
print(list3)

'''
所谓的返回值就是运行完这个表达式后，他会有一串值输出来，如果我们用新的变量去接住这个返回值，那么这个变量的值就是返回出来的值。
'''


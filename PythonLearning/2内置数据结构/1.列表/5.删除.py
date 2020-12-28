# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 22:55
# @Author  : wanghc
# @File    : 5.删除.py
# @Software: PyCharm

# 5.1 list.remove
# help(list.remove)
'''
    L.remove(value) -> None -- remove first occurrence of value.
    Raises ValueError if the value is not present.
删除第一个匹配的元素，无返回值
'''
l = [1, 2, 3, 4, 5, 4, 3, 2, 1]
l.remove(1)  # 从左往右删除第一个，原地修改，返回None，根据值删除元素。
print(l)

# 5.2 list.pop
# help(list.pop)
'''
  L.pop([index]) -> item -- remove and return item at index (default last).
  Raises IndexError if list is empty or index is out of range.
不传入参数，默认返回并删除最后一个值，传入Index参数，返回并删除index所在的元素。
'''
l2 = [5, 6, 7, 8]
x = l2.pop()
y = l2.pop(2)
print(l2)
print(x)
print(y)

'''
pop 不传递index函数,时间复杂度是O(1)
pop 传递index函数,时间复杂度是O(n)
pop 根据索引删除元素，并且返回删除的元素
remove 根据值删除元素,返回None
'''

# 5.3 list.clear
# help(list.clear)
'''
clear(...)
    L.clear() -> None -- remove all items from L
删除所有的元素
'''
lc = [3, 3, 3, 3]
lc.clear()
print(lc)  # []  使用clear之后，列表对象还在，只是里面的值被清空了

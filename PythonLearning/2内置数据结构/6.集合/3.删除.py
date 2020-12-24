# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 11:31
# @Author  : wanghc
# @File    : 3.删除.py
# @Software: PyCharm

# 1.remove
# print(help(set.remove))

'''
remove(...)
    Remove an element from a set; it must be a member.
    
    If the element is not a member, raise a KeyError.
    1.会从集合中删除传入的变量，但是这个变量必须是集合中的元素
    2.如果这个元素不存在，是会抛出异常的，这是需要注意的
    3.原地修改，不返回值
'''

s = {1,2,3,4,5}
s.remove(5)
print(s)
#s.remove(0) # KeyError: 0
print(s)


# 2.pop
# print(help(set.pop))
'''
pop(...)
    Remove and return an arbitrary set element.  会返回被删除的值
    Raises KeyError if the set is empty.    但集合空了，会抛出keyerror信息
'''
x = s.pop()
print(x)
y = s.pop()
print(y)

# s.clear()
# s.pop() # KeyError: 'pop from an empty set'


# 3.discard
# print(help(set.discard))
'''
discard(...)
    Remove an element from a set if it is a member.     可以选择想要删除的元素，原地修改，不返回值        
    
    If the element is not a member, do nothing.
'''
se = {'whc','hxx','xxx'}
se.discard('xxx')
print(se)
se.discard('yyy') # 删除不存在的元素时，什么也不做
print(se)


'''
总结：
remove:删除给定的元素，元素不存在抛出keyerror
discard:删除给定的元素，元素不存在什么都不做
pop:随机删除一个元素并返回，集合为空，抛出keyerror
clear:清空集合
'''

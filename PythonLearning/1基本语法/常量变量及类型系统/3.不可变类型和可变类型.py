# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 8:13
# @Author  : wanghc
# @File    : 3.不可变类型和可变类型.py
# @Software: PyCharm

# 1.不可变类型
'''
变量对应的值不能被修改，如果修改就会生成一个新的值从而分配新的内存空间

不可变类型：
数字（int,long,float）
布尔（bool）
字符串（string）
元组（tuple）
'''

# 案例一
n = 5
x = n

print(id(n))
n += 1   #修改n的值将会生成新的值重新赋值给n
print(id(n))

# 案例二
b = True
print(id(b))
b = not True
print(id(b))


# 2.可变类型    list、dict
'''
变量对应的值中的数据可以被改变，但内存地址保持不变。
'''
l = [1,2,3]
print(id(l))
l.append(4)
print(id(l))

star = {"name":'whc',"age":20}
print(id(star))
star["age"] = 25
print(id(star))


'''
为什么会出现以上2种情况？

因为python中的值是通过 引用 （地址值）传递的，不可变类型的值一旦被修改后会创建一个内存空间并生成新的地址值。
可变类型的值会在原内存空间中被修改。
'''

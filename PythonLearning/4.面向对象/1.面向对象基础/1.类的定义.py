# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 16:06
# @Author  : wanghc
# @File    : 1.类的定义.py
# @Software: PyCharm

from collections import namedtuple

# namedtuple 可以用来组织数据

#Door = namedtuple('Door', ['number', 'status'])

#door = Door(1001, 'closed')

#print(door.number)

'''
但是当需要定义动作的时候，namedtuple是做不到的，这时候就可以用类
'''

'''
class关键字用来定义一个类，后面加类名和分号
'''

class Door:
    def __init__(self, number, status):
        self.number = number
        self.status = status


door = Door(1301,'closed')

print(door.number)   # 1301
print(door.status)   # closed


'''
探索一下，init函数
'''

class B:
    def __init__(self):
        print('a')
        print('b')

b = B() # 控制台打印  a  b

'''
发现类初始化的时候，会执行init函数。

现在可以得出如下结论：
1.创建对象使用 类名（__init__函数除第一参数外的参数列表）
2.创建对象的时候实际执行了init函数
'''



# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 10:12
# @Author  : wanghc
# @File    : 2.抛出异常.py
# @Software: PyCharm


'''
异常是由程序自己抛出的，我们上面看到的open就是
目前大多数的标准库都是程序自己来处理异常的。如何抛出异常？
用raise语句： raise + 特殊类的实例
'''

# raise Exception()   这就是抛出异常了，抛出异常就是通知调用者，此处发生了意外

def fn():
    print('start')
    raise Exception()
    print('end')

fn() # 抛出异常会提前返回，输出start后，就抛出异常，不会输出end。所以说抛出异常是安全的 。



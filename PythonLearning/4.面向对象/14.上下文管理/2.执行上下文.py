# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 20:54
# @Author  : wanghc
# @File    : 2.执行上下文.py
# @Software: PyCharm

class Context:
    def __enter__(self):
        print('enter context')

    def __exit__(self, *args, **kwargs):
        print('exit context')


with Context():
    print('do something')

print('out of context')

'''
打印：
enter context
do something
exit context
out of context

上下文：
with关键字会开启一个语句块
执行这个语句块之前，会执行__enter__方法
执行这个语句块之后，会执行__exit__方法

也就是说这个语句块的前后会执行一些操作。
'''

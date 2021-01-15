# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 20:50
# @Author  : wanghc
# @File    : 1.定义.py
# @Software: PyCharm

'''
支持上下文管理的对象可以使用

with obj:
    pass

'''


class Context:
    def __enter__(self):
        print('enter context')

    def __exit__(self, *args, **kwargs):
        print('exit context')


'''
当一个对象同时实现了一个__enter__和__exit__方法，那么这个对象就是支持上下文管理的对象。
'''


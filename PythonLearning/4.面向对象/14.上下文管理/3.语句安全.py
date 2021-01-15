# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 21:09
# @Author  : wanghc
# @File    : 3.语句安全.py
# @Software: PyCharm

class Context:
    def __enter__(self):
        print('enter context')

    def __exit__(self, *args, **kwargs):
        print('exit context')


with Context():
    raise Exception()

'''
发现即使是抛出异常，__enter__和__exit__方法也是执行的。
所以我们的上下文管理是安全的。
'''

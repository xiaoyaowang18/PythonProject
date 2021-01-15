# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 21:16
# @Author  : wanghc
# @File    : 4.as对象.py
# @Software: PyCharm

class Context:
    def __enter__(self, *args, **kwargs):
        print('enter context')
        return '哈哈哈'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit context')
        print('exception:{}'.format(exc_type))
        print('tracetrack:{}'.format(exc_tb))
        return 'exit返回值'


ctx = Context()

with ctx as c:
    print(id(ctx))
    print(id(c))
    print(c)

'''
文件对象就是我们的self，__enter__方法的返回值可以通过as获取
'''

'''
enter能不能有参数？   从打印结果来看，不带任何参数

exit的返回值没有被任何对象所接受，没有办法获取到。
第一个参数是异常type，第二个是异常实体exception，第三个是异常追踪track
但是通常不会在exit中处理异常
'''

with Context():
    raise Exception()


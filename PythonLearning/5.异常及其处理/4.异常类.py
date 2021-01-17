# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 10:23
# @Author  : wanghc
# @File    : 4.异常类.py
# @Software: PyCharm

'''
python解释器提供了一个BaseException的类，所有的子类都是异常类
'''

# Exception就是BaseException的子类

# print(Exception.__mro__)  (<class 'Exception'>, <class 'BaseException'>, <class 'object'>)

# print(TypeError.__mro__)   (<class 'TypeError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)

# print(AttributeError.__mro__)  (<class 'AttributeError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)

try:
    raise TypeError
except Exception:
    print('exception')

# except 后面可以跟一个异常类，这时候，他仅仅捕获此类及子类的异常。

'''
为什么要有except这个模式匹配呢？
因为except的模式匹配，可以针对不同的异常做不同的处理
事实上，一个try语句，可以带多个except语句

越特殊的异常类应该越放到前面，越一般的异常类应该越放到后面
'''

try:
    raise TypeError()
except TypeError:
    print('Type Error')
except AttributeError:
    print('attribute error')
except Exception:
    print('exception')

'''
再说一个能力。
except 可以带一个as子句，获取异常类的实例
raise抛出的是实例
在抛出异常的时候，可以给异常处理代码传递一些信息
'''

class CustomException(Exception):
    def __init__(self,code,message):
        self.code = code
        self.message = message

try:
    raise CustomException(500,'some error')
except CustomException as e:
    print('<{}> {}'.format(e.code,e.message))
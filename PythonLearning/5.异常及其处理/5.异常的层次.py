# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 10:53
# @Author  : wanghc
# @File    : 5.异常的层次.py
# @Software: PyCharm

'''
Exception.__mro__继承BaseException

还有哪些是继承BaseException呢？
'''

# 1.表示按下ctrl c 会触发这个异常，这个异常通常是在控制程序退出的时候会用到
print(KeyboardInterrupt.__mro__)  # (<class 'KeyboardInterrupt'>, <class 'BaseException'>, <class 'object'>)


def loop():
    while True:
        pass


# try:
#   loop()
# except KeyboardInterrupt:
#  pass


# 2.SystemExit  调用sys.exit会抛出此异常，通常用于退出解释器
print(SystemExit.__mro__)

# 3.GeneratorExit 生成器退出时，抛出此异常

'''
事实上，python标准库里，只有这4个异常直接继承自BaseException，而这3个都是有特殊含义的吧

通常来说自定义异常不会直接继承BaseException

标准库里的其他异常，直接或间接继承自Exception

如果遵循这些规范的话，可以用 except Exception as e 来捕获所有异常
'''

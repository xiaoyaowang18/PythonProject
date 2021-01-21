# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 20:34
# @Author  : wanghc
# @File    : 6.name属性.py
# @Software: PyCharm


if __name__ == '__main__':
    print('this is main module')


'''
当我们直接执行它的时候，它的name是'__main__'，所以就会直接执行这个代码

而import进来的时候，显示的时候是一个模块名，就不会被执行了

通常把一些简单的测试代码放在这里，但是这个不等于单元测试
'''
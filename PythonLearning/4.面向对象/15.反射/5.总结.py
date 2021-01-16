# -*- coding: utf-8 -*-
# @Time    : 2021/1/16 12:05
# @Author  : wanghc
# @File    : 5.总结.py
# @Software: PyCharm

'''
反射是动态给实例添加属性的方法

python内置函数：
getattr & setattr & hasattr
用的最多的就是getattr，用来获取实例的属性和方法，非常方便

而__getattr__ & __setattr__ &  __delattr__是作用在类里的

当一个类想要对属性的获取，修改，删除做一些自定义的操作，可以通过这三个方法

建议不要用__getattribute__
'''

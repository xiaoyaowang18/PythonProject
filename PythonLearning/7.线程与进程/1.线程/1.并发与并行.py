# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 20:51
# @Author  : wanghc
# @File    : 1.并发与并行.py
# @Software: PyCharm

'''
并发：
假同时，一段时间内看起来是同时，一段时间内同时处理多个任务

并行：
真同时，同时处理多个任务

区别就是一段时间，因为并发在单核里也可以，并行必须要多核

为什么在单核中也可以并发呢？

因为它是假同时，把任务切分成多个时间片，然后这些任务在交替的时间片上执行了，称为并发。

实现并发的手段：
1.线程   2.进程

主流的语言通常提供用户空间的调度，称为协程

python在3.5开始支持我们的协程了。
'''



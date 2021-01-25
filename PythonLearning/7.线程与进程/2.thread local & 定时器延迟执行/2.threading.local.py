# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 20:22
# @Author  : wanghc
# @File    : 2.threading.local.py
# @Software: PyCharm

import threading
import logging
import importlib

importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')

cl = threading.local()  # cl没有任何属性

cl.data = 5

data = 'aaa'

def work():
    logging.info(cl.data)
    logging.info(data)

t = threading.Thread(target=work)

t.start()

'''
AttributeError: '_thread._local' object has no attribute 'data'
报错没有data这个对象

这是因为ctx是一个thread local的变量，我们可以给他赋值任何属性，但是只能在当前线程可见。

线程独享资源
'''
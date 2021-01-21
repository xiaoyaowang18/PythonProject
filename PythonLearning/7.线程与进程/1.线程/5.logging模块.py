# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 21:25
# @Author  : wanghc
# @File    : 5.logging模块.py
# @Software: PyCharm


import logging

logging.warning('哈哈哈')
logging.error('error')

# info没有
logging.info('info')

# 因为在logging中有一个基本的log级别需要配置
import importlib
importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)s %(threadName)s %(message)s')
logging.info('info')

# 来看一下logging是不是线程安全的
def work(num):
    logging.warning('warning-{}'.format(num))

import threading
for x in range(5):
    t = threading.Thread(target=work,args=(x,))
    t.start()

'''
通常会用Logging代替print，因为logging是线程安全的，在多线程里也能正常表现。
'''
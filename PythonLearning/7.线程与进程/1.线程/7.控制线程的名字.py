# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 22:18
# @Author  : wanghc
# @File    : 7.控制线程的名字.py
# @Software: PyCharm

'''
通过name参数控制线程名字
'''
import logging
import time
import threading
import importlib
importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')


def worker():
    logging.info('starting')
    time.sleep(2)
    logging.info('completed')

t1 = threading.Thread(target=worker,name = 'first')
t2 = threading.Thread(target=worker,name = 'first')
t1.start()
t2.start()


'''
线程可以重名，线程名不是线程的唯一标识，但是通常应该避免线程重名，通常处理手段是加前缀
'''
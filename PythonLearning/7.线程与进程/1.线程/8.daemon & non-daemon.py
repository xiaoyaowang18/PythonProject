# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 22:25
# @Author  : wanghc
# @File    : 8.daemon & non-daemon.py
# @Software: PyCharm
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

t1 = threading.Thread(target=worker,name = 'first',daemon=True)

t1.start()

'''
打开daemon=True
瞬间就执行完了,completed没有打印出来，不会等待执行。
'''


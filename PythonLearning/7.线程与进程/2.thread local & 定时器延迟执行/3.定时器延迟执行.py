# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 20:35
# @Author  : wanghc
# @File    : 3.定时器延迟执行.py
# @Software: PyCharm


import threading
import logging
import importlib

importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')


def work():
    logging.info('run')


# 过5秒执行了一条
t = threading.Timer(interval=5, function=work)
t.start()


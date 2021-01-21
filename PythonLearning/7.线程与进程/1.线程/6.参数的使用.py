# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 22:02
# @Author  : wanghc
# @File    : 6.参数的使用.py
# @Software: PyCharm

import logging
import threading
import importlib

importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')


def add(x, y):
    logging.info(x + y)


# 通过args传递位置参数或者kwargs传递关键字参数都是可以的
threading.Thread(target=add, args=(1, 2)).start()
threading.Thread(target=add, kwargs={'x': 1, 'y': 2}).start()
threading.Thread(target=add, args=(1,), kwargs={'y': 2}).start()

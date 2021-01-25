# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 21:10
# @Author  : wanghc
# @File    : 2.event.py
# @Software: PyCharm

'''
event = threading.Event()
有一个set方法和wait方法

wait方法会阻塞线程，直到set方法被调用
'''

import threading
import time
import random
import datetime
import logging
import importlib

importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')



def worker(event: threading.Event):
    time.sleep(random.randint(1, 5))
    print('第一次')
    event.set()
    print(event.is_set())

def boss(event: threading.Event):
    start = datetime.datetime.now()
    event.wait()
    logging.info('work exit {}'.format(datetime.datetime.now() - start))

def start():
    event = threading.Event()
    b = threading.Thread(target=boss,args=(event,),name = 'boss')
    b.start()
    for x in range(5):
        threading.Thread(target=worker,args=(event,),name = 'worker').start()

start()

'''
第一次
2021-01-25 21:28:29,550 INFO boss work exit 0:00:02.012316
第一次
第一次
第一次
第一次

event.wait会阻塞线程，直到set方法被调用。  当第一次work方法执行时，event.set调用后，boss马上就打印出日志。

所以event可以在线程之间发送信号。

通常用于某个线程需要等待其他线程处理完成某些动作之后才能启动。
'''
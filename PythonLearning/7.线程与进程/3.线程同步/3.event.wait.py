# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 21:46
# @Author  : wanghc
# @File    : 3.event.wait.py
# @Software: PyCharm
import threading
import time
import random
import datetime
import logging
import importlib

importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')


def work(event:threading.Event):
    while not event.wait(3):
        logging.info('run run run')

event = threading.Event()

threading.Thread(target=work,args=(event,),name='print').start()


'''
默认情况下，event.wait总是false的，所以我们需要给她一个set，他就变成true，也就退出循环了

event.is_set()  event.set调用后返回True
event.clear() 清除set标志，之前的is_set变成false
'''



'''
event.wait(3)和sleep的区别？

wait会主动让出时间片
sleep不会

假如时间片是30ms,wait用掉了10ms，然后就让出来了。
但是sleep会让出剩下的20ms
'''
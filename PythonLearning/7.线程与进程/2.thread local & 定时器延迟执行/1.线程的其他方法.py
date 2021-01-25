# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 20:06
# @Author  : wanghc
# @File    : 1.线程的其他方法.py
# @Software: PyCharm

import threading
import logging
import importlib

importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')

# enumerate方法可以获取所有线程
# print(threading.enumerate())  # [<_MainThread(MainThread, started 4208)>]

'''
刚才的线程都是通过实例化Thread类，既然Thread是一个类，我们是不是可以通过继承来处理？
'''

class MyThread(threading.Thread):
    def run(self):
        logging.info('run')


#t = MyThread()
#t.run()

'''
当我们一个类继承了我们的thread类，是可以实现线程的，但是python通常不使用这种方法。
'''

def work():
    print('work')

t = threading.Thread(target=work)

t.start()
# t.run()
'''
如果不是以继承的方式创建线程 ， run方法和start方法只能执行其中一个，而且run方法不会启动线程，start方法才会。为什么呢？
'''
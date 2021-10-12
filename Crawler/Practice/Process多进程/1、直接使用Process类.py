# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 15:13
# @Author  : wanghc
# @File    : 1、直接使用Process类.py
# @Software: PyCharm

import multiprocessing


def process(index):
    print(f'Process: {index}')


if __name__ == '__main__':

    for i in range(5):
        '''
        这里 args 必须要是一个元组，如果只有一个参数，那也要在元组第一个元素后面加一个逗号，
        如果没有逗号则和单个元素本身没有区别，无法构成元组，导致参数传递出现问题。
        '''
        p = multiprocessing.Process(target=process, args=[i])
        p.start()
    print(f'CPU number: {multiprocessing.cpu_count()}')  # CPU核数
    for p in multiprocessing.active_children():  # 当前正在活跃运行的进程列表
        print(f'Child process name: {p.name} id: {p.pid}')
    print('Process Ended')

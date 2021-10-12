# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 17:07
# @Author  : wanghc
# @File    : 10、进程池.py
# @Software: PyCharm

from multiprocessing import Pool

import time
import urllib

'''
假如现在我们遇到这么一个问题，我有 10000 个任务，每个任务需要启动一个进程来执行，并且一个进程运行完毕之后要紧接着启动下一个进程，
同时我还需要控制进程的并发数量，不能并发太高，不然 CPU 处理不过来（如果同时运行的进程能维持在一个最高恒定值当然利用率是最高的）。

那么我们该如何来实现这个需求呢？

用 Process 和 Semaphore 可以实现，但是实现起来比较我们可以用 Process 和 Semaphore 解决问题，但是实现起来比较烦琐。
而这种需求在平时又是非常常见的。此时，我们就可以派上进程池了，即 multiprocessing 中的 Pool。
Pool 可以提供指定数量的进程，供用户调用，当有新的请求提交到 pool 中时，如果池还没有满，就会创建一个新的进程用来执行该请求；
但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来执行它。
'''


def function(index):
    print(f'Start process: {index}')

    time.sleep(3)

    print(f'End process {index}', )


if __name__ == '__main__':

    pool = Pool(processes=3)

    for i in range(4):
        pool.apply_async(function, args=(i,))

    print('Main Process started')

    pool.close()

    pool.join()

    print('Main Process ended')


def scrape(url):
    try:
        urllib.request.urlopen(url)
        print(f'URL {url} Scraped')
    except (urllib.error.HTTPError, urllib.error.URLError):
        print(f'URL {url} not Scraped')


if __name__ == '__main__':
    pool = Pool(processes=3)
    urls = [
        'https://www.baidu.com',
        'http://www.meituan.com/',
        'http://blog.csdn.net/',
        'http://xxxyxxx.net'
    ]
    '''
    第 1 个参数就是进程对应的执行方法，第 2 个参数就是 urls 列表，
    map 方法会依次将 urls 的每个元素作为 scrape 的参数传递并启动一个新的进程，加到进程池中执行。
    '''
    pool.map(scrape, urls)
    pool.close()

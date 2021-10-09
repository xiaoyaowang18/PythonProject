# -*- coding: utf-8 -*-
# @Time    : 2021/9/29 17:25
# @Author  : wanghc
# @File    : 超时设置.py
# @Software: PyCharm

import requests


'''
在本机网络状况不好或者服务器网络响应延迟甚至无响应时，我们可能会等待很久才能收到响应，甚至到最后收不到响应而报错。
为了防止服务器不能及时响应，应该设置一个超时时间，即超过了这个时间还没有得到响应，那就报错。这需要用到 timeout 参数。这个时间的计算是发出请求到服务器返回响应的时间。
'''

import requests



r = requests.get('https://httpbin.org/get', timeout=1)

print(r.status_code)


'''
通过这样的方式，我们可以将超时时间设置为 1 秒，如果 1 秒内没有响应，那就抛出异常。

实际上，请求分为两个阶段，即连接（connect）和读取（read）。

上面设置的 timeout 将用作连接和读取这二者的 timeout 总和。

如果要分别指定，就可以传入一个元组

r = requests.get('https://httpbin.org/get', timeout=(5, 30))
'''

'''
如果想永久等待，可以直接将 timeout 设置为 None，或者不设置直接留空，因为默认是 None。
这样的话，如果服务器还在运行，但是响应特别慢，那就慢慢等吧，它永远不会返回超时错误的。其用法如下：

r = requests.get('https://httpbin.org/get', timeout=None)
'''


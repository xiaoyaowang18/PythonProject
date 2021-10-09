# -*- coding: utf-8 -*-
# @Time    : 2021/9/29 17:31
# @Author  : wanghc
# @File    : 代理设置.py
# @Software: PyCharm

import requests

'''
1、
某些网站在测试的时候请求几次，能正常获取内容。但是对于大规模且频繁的请求，网站可能会弹出验证码，或者跳转到登录认证页面，更甚者可能会直接封禁客户端的 IP，导致一定时间段内无法访问。

为了防止这种情况发生，我们需要设置代理来解决这个问题，这就需要用到 proxies 参数。
'''

import requests



proxies = {

  'http': 'http://10.10.10.10:1080',

  'https': 'http://10.10.10.10:1080',

}

requests.get('https://httpbin.org/get', proxies=proxies)


'''
2、若代理需要使用上文所述的身份认证，可以使用类似 http://user:password@host:port 这样的语法来设置代理，示例如下
'''
import requests

proxies = {'https': 'http://user:password@10.10.10.10:1080/',}

requests.get('https://httpbin.org/get', proxies=proxies)


'''
3、除了基本的 HTTP 代理外，requests 还支持 SOCKS 协议的代理。

首先，需要安装 socks 这个库
'''
import requests


proxies = {

    'http': 'socks5://user:password@host:port',

    'https': 'socks5://user:password@host:port'

}

requests.get('https://httpbin.org/get', proxies=proxies)

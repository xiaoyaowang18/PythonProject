# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 16:13
# @Author  : wanghc
# @File    : 10.remove.py
# @Software: PyCharm


'''
顾名思义，remove 方法就是移除，它有时会为信息的提取带来非常大的便利。下面有一段 HTML 文本

官方文档：http://pyquery.readthedocs.io/en/latest/api.html。
'''

html = '''

<div class="wrap">

    Hello, World

    <p>This is a paragraph.</p>

 </div>

'''

from pyquery import PyQuery as pq

doc = pq(html)

wrap = doc('.wrap')

wrap.find('p').remove()

print(wrap.text())

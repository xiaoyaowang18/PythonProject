# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 16:19
# @Author  : wanghc
# @File    : 11.伪类选择器.py
# @Software: PyCharm

'''
http://www.w3school.com.cn/css/index.asp。
'''

html = '''

<div class="wrap">

    <div id="container">

        <ul class="list">

             <li class="item-0">first item</li>

             <li class="item-1"><a href="link2.html">second item</a></li>

             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>

             <li class="item-1 active"><a href="link4.html">fourth item</a></li>

             <li class="item-0"><a href="link5.html">fifth item</a></li>

         </ul>

     </div>

 </div>

'''

from pyquery import PyQuery as pq

doc = pq(html)


'''
依次选择了第 1 个 li 节点、
最后一个 li 节点、
第 2 个 li 节点、
第 3 个 li 之后的 li 节点、
偶数位置的 li 节点、
包含 second 文本的 li 节点。
'''

li = doc('li:first-child')

print(li)

li = doc('li:last-child')

print(li)

li = doc('li:nth-child(2)')

print(li)

li = doc('li:gt(2)')

print(li)

li = doc('li:nth-child(2n)')

print(li)

li = doc('li:contains(second)')

print(li)

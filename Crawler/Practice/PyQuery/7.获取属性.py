# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 15:47
# @Author  : wanghc
# @File    : 7.获取属性.py
# @Software: PyCharm


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

a = doc('.item-0.active a')

print(a, type(a))

print(a.attr('href'))


'''
在进行属性获取时，先要观察返回节点是一个还是多个，如果是多个，则需要遍历才能依次获取每个节点的属性。
'''
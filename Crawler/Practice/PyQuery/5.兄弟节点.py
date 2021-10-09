# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 15:27
# @Author  : wanghc
# @File    : 5.兄弟节点.py
# @Software: PyCharm

html = '''

<div id="container">

    <ul class="list">

         <li class="item-0">first item</li>

         <li class="item-1"><a href="link2.html">second item</a></li>

         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>

         <li class="item-1 active"><a href="link4.html">fourth item</a></li>

         <li class="item-0"><a href="link5.html">fifth item</a></li>

     </ul>

 </div>

'''

from pyquery import PyQuery as pq

doc = pq(html)

'''
首先选择 class 为 list 的节点，内部 class 为 item-0 和 active 的节点，也就是第 3 个 li 节点。
很明显，它的兄弟节点有 4 个，那就是第 1、2、4、5 个 li 节点。
'''
li = doc('.list .item-0.active')

#print(li.siblings())

'''
我们依然可以用 siblings 方法传入 CSS 选择器，这样就会从所有兄弟节点中挑选出符合条件的节点了
'''
print(li.siblings('.active'))
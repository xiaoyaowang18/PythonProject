# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 14:56
# @Author  : wanghc
# @File    : 4.父节点.py
# @Software: PyCharm

from pyquery import PyQuery as pq

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

doc = pq(html)

items = doc('.list')

'''
1、获取class为list的节点的父节点
'''
container = items.parent()

print(type(container))

print(container)

'''
2、获取祖先节点
'''
parents = items.parents()
print(parents)

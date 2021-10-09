# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 16:05
# @Author  : wanghc
# @File    : 9.节点操作.py
# @Software: PyCharm

from pyquery import PyQuery as pq

'''
1、addClass和removeClass
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


doc = pq(html)

li = doc('.item-0.active')

print(li)

li.removeClass('active')

print(li)

li.addClass('active')

print(li)


'''
2、attr、text、html
'''
html = '''

<ul class="list">

     <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>

</ul>

'''

from pyquery import PyQuery as pq

doc = pq(html)

li = doc('.item-0.active')

print(li)

li.attr('name', 'link')

print(li)

li.text('changed item')

print(li)

li.html('<span>changed item</span>')

print(li)


























# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 14:28
# @Author  : wanghc
# @File    : 3.子节点.py
# @Software: PyCharm

from pyquery import PyQuery as pq

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

doc = pq(html)
items = doc('.list')
#print(type(items))
#print(items)

'''
find方法会将符合条件的所有节点选择出来，查找范围是节点的所有子孙节点，如果只想查找子节点，可以使用children方法
'''
items_find = items.find('li')
#print(type(items_find))
#print(items_find)

items_children = items.children()
#print(items_children)


'''
如果要筛选所有子节点中符合条件的节点，比如想要筛选子节点中class为active的节点，可以向children中传入css选择器
'''
children = items.children('.active')
print(children)

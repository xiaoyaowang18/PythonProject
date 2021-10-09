# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 15:43
# @Author  : wanghc
# @File    : 6.遍历.py
# @Software: PyCharm

from pyquery import PyQuery as pq
'''
通过刚才的例子我们可以观察到，pyquery 的选择结果既可能是多个节点，也可能是单个节点，类型都是 pyquery 类型，并没有返回列表。
'''

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

lis = doc('li').items()

print(type(lis))

for li in lis:

    print(li, type(li))

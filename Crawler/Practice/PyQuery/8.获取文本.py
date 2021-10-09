# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 15:56
# @Author  : wanghc
# @File    : 8.获取文本.py
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

print(a)

print(a.text())

'''
首先选中一个 a 节点，然后调用 text 方法，就可以获取其内部的文本信息了。text 会忽略节点内部包含的所有 HTML，只返回纯文字内容。
'''


li = doc('li')
print(li.html())
print(li.text())
print(type(li.text()))

'''
html 方法返回的是第 1 个 li 节点的内部 HTML 文本，而 text 则返回了所有的 li 节点内部的纯文本，中间用一个空格分割开，即返回结果是一个字符串。
'''

li = doc('.item-0.active')
print(li.html())
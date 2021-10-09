# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 11:16
# @Author  : wanghc
# @File    : 1.初始化.py
# @Software: PyCharm

from pyquery import PyQuery as pq

'''
1、字符串初始化
'''

html = '''
<div>

    <ul>

         <li class="item-0">first item</li>

         <li class="item-1"><a href="link2.html">second item</a></li>

         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>

         <li class="item-1 active"><a href="link4.html">fourth item</a></li>

         <li class="item-0"><a href="link5.html">fifth item</a></li>

     </ul>

 </div>
'''

'''
将一个长html字符串，将其当参数传递给pyquery类，完成初始化
'''
#doc = pq(html)

'''
传入css选择器，传入li节点，这样就可以选择所有的li节点
'''
#print(doc('li'))



'''
2、url初始化
'''
doc = pq(url='https://cuiqingcai.com')
print(doc('title'))


'''
3、文件初始化
'''
doc = pq(filename='demo.html')
print(doc('li'))

# -*- coding: utf-8 -*-
# @Time    : 2020/1/20 17:51
# @Author  : wanghc
# @File    : 2.转义.py
# @Software: PyCharm

# 什么是转义？
'''
所有的ASCII码都可以用'\'加数字（一般是8进制数字）来表示。
而C中定义了一些字母前加'\'来表示常见的那些不能显示的ASCII字符，如\o,\t,\n等，就称为转义字符，因为后面的字符，都不是它本来的ASCII码的意思了
'''

#  1.简单转义 \n  换行符
s = '人人都是\nPythonista'
print(s)

# 2.单引号里包括一段话，这段话里也有单引号，就需要转义了
s = 'I\'m pythonista'
print(s)

# 3.如果既有单引号又有双引号，那就用三引号包含咯

# 4.如何避免一直去转义，更关键的是有时候我作为服务端，不知道客户端传给我的是什么，又如何去一个个对应的转义呢？
'''
这个时候可以用上python的一个前缀关键字 r ，它表示：后面的这个字符串是raw string,也就是纯纯的字符串,不会有其他意思了。
'''
path = r'C:\windows\nt\system32'
print(path)

# 5.补充
'''
python3中字符串类型str就是以Unicode编码格式编码，所以我们在Python3 中看到多种语言文字的字符串而不会出现乱码。
编码是一种用一种特定的方式对抽象字符（Unicode）转换为二进制形式（bytes）进行表示，也就是python3中的encode。
解码就是对用特定方式表示的二进制数据用特定的方式转化为Unicode，也就是decode。
u前缀代表unicode字符串
b前缀代表bytes
'''
s = u'哈哈哈'.encode()
print(s)
s = b'hehe'.decode()
print(s)


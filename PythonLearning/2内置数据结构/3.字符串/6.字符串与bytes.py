# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 16:45
# @Author  : wanghc
# @File    : 6.字符串与bytes.py
# @Software: PyCharm


'''
1.定义
string是文本序列
bytes是字节序列

1.1区别
文本是有编码的，例如：utf-8、gbk、GB18030等。
字节没有编码
文本的编码指的是字符如何使用字节来表示

1.2编码
单字节编码，例如:ascii
多字节编码，例如：utf-8

编码是信息从一种格式或格式转换为另一种形式的过程，
python3中，字符串默认使用Utf-8编码
字符串经过编码后的数据类型，称之为bytes
'''

s = '人人都是pythonista'
# 默认utf-8编码
s2 = s.encode()
print(s2)  # b'\xe4\xba\xba\xe4\xba\xba\xe9\x83\xbd\xe6\x98\xafpythonista'

# '人人都是' 这几个字每个字符有3个字节（3个16进制数组成）

# encode也可以是其他字节，比如用gbk做我们的编码字符集，与utf-8出来的字节不同，每个字符2个字节
s3 = s.encode('gbk')
print(s3) # b'\xc8\xcb\xc8\xcb\xb6\xbc\xca\xc7pythonista'

# bytes转换成字符串,使用decode进行解码
s4 = s2.decode()
print(s4) # 人人都是pythonista
# 也可以转成其他的编码格式
s5 = s2.decode('gbk')
print(s5) # 浜轰汉閮芥槸pythonista  乱码，就是无法转换，因为原来的是utf-8的。gbk双字节，utf-8三字节，不对应。


'''
为什么要用编码？
服务器 linux utf-8 
客户端 windows gbk
通过socket通信
当客户端发送一个gbk字符串给linux服务器，linux就需要转码了，否则就乱了。
因为客户端本地是gbk，服务端要用decode utf8肯定失败的。这时候就需要约定好是gbk，不能是utf-8
否则字符串传递过来（编码成字节后），没有办法解码。   
在python3中，socket只能用bytes
'''

# bytes
'''
string的所有操作，bytes都支持
bytes可由string的encode方法得到
可以通过前缀b定义bytes
'''
bt = b'\xe4\xba\xba'
print(type(bt))
print(len(bt))
print(bt.decode())

# bytes操作
# 传入参数也必须是bytes,如果传入字符串会报错
x = bt.find(b'\xba')
print(x)
hex = bt.hex()  # 转为16进制
print(hex)


# bytearray
'''
bytearray是bytes的可变版本
str和bytes是不可变的
'''
byt = '人人都是pythonista'.encode()
print(byt)
print(byt[0])

bytarr = bytearray(byt)
print(bytarr)

# byte不可变  bytearray可变
# byt[0] = b'aaa'   TypeError: 'bytes' object does not support item assignment  赋值会报错
ba = bytearray(b'abc')
ba[0] = int(b'D'.hex(),16) # bytearray更新的时候也是一个个字节更新的，不是一个字符串，要把字节转换成十六进制数进行更替
print(ba)

'''
使用场景：为什么需要byte可变？
因为有一种数据处理：图像处理
当需要修改图片时，比如灰度处理，图像保存成了字节，因为bytes不可变，当图片修改一处是3M,修改一百处就是300M,对图片的像素级修改，内存占用这么高肯定不行
因此我们需要对大对象的二进制做修改，需要一个可变版本的bytes    
'''

# bytearray的方法
# 相对bytes来说，多了Insert，append,extend,pop,remove,clear,reverse，多出了list的方法，并可以索引操作
ba = bytearray(b'abc')
# 修改bytearray时，所有的方法中需要用int来表示，而非bytes本身
# ba.insert(b'E',0) TypeError: 'bytes' object cannot be interpreted as an integer
ba.insert(int(b'E'.hex(),16),0)
ba.append(20)
print(ba)

# insert append remove count的参数必须是int，且范围在0~256
ba.append(257) # ValueError: byte must be in range(0, 256)
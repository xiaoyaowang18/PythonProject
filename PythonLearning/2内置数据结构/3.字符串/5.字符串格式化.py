# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 16:07
# @Author  : wanghc
# @File    : 5.字符串格式化.py
# @Software: PyCharm

'''
字符串格式化是拼接字符串的一种手段
'''

'''
1.join拼接字符串  但是有个问题,join拼接难以控制格式
'''
l = ['i','love','you']
s = ''.join(l)
print(s)

'''
2.print style 字符串格式化
通过占位符来达到字符替换的作用
占位符：%，加一个格式控制符
例如： s = '人人都是%s'
接着在字符串后面追加一个%,再追加一个元组，元组里面加上要组合的字符串，注意：字符串个数需要和%s相同
'''
s = '人人都是%s'
s = s%('哈哈哈',)
print(s)

h = 'i love %s , i am %d'
h2 = h % ('python',18)
print(h2)

# 当占位符是%s的时候，隐式调用了str()
h3 = h % (18,18)
print(h3)

# %r 隐式调用 repr()
x = '%r' % 18
print(x)

# str() 和 repr()的区别

# 当拼接字符串的时候，一定要用这种print style, %的方式可以帮助我们避免恶意sql注入

'''
3.format使用大括号作为占位符
当使用format的时候，format传入的参数会替换大括号
'''
s = '人人都是{}'
s = s.format('哈哈哈')
print(s)

'''
format方法的参数个数是可变的
'''
s2 = 'i love {} i am {}'
s2 = s2.format('python',18)
print(s2)

'''
可以占位符里加数字，指定format参数的位置
'''
s3 = 'i love {1}, i am {0}'
s3 = s3.format(18,'python')
print(s3)

'''
参数可以通过指定位置方式多次使用
'''
s4 = '{0},{0}'.format('人人都是pythonista')
print(s4)

'''
可以占位符里加标识符，使用关键字参数
'''
s5 = '{who} {do} {what}'.format(who='人人',do='都是',what='pythonista')
print(s5)

'''
同时支持位置和关键字参数,位置参数需要在前面
'''
s6 = '{0}{who}{do}{what}'.format('今天',who='人人',do='都是',what='pythonista')
print(s6)

'''
占位符和参数不匹配，会抛出异常，超出不行
'''
#s7 = '{1}{2}{3}'.format('dd','aa','dd')
#print(s7)

'''
小结：
{}按照顺序，使用位置参数
{数字i}会把位置参数当成一个列表args,args[i],当i不是args的索引的时候，抛出indexerror
{关键字key}会把关键字参数当成一个字典kwagrs，使用kwargs[k]，当key不是kwargs的key时，会抛出keyerror
'''
# 打印{}
print('{{}}'.format())
print('{{{}}}'.format(18))


'''
4. f前缀
'''
who = '人人'
do = '都是'
whom = 'pythonista'
print(f'{who}{do}{whom}')

'''
当写服务端，客户端的时候，不知道传递过来的值是怎么样的，往往会用一个变量去接住客户端传来的某个参数
'''
token = 'dafdfasfsaf'
user_id = '1'
dt = '2009-12-07'
url = f'http://dsafa.com/token={token}&user_id={user_id}&dt={dt}'
print(url)


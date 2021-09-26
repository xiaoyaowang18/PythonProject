# -*- coding: utf-8 -*-
# @Time    : 2020/1/22 11:10
# @Author  : wanghc
# @File    : 4.字符串的操作.py
# @Software: PyCharm

# 1.join
'''
join是字符串的方法，参数是可迭代对象，接受者是分隔符
join前面的这个字符串就是分隔符了，用这个分隔符把列表里的每个元素都拼起来

   def join(self, iterable): # real signature unknown; restored from __doc__
        """
        S.join(iterable) -> str

        Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.
        """
        return ""
'''
l = ['人人', '都是', 'pythonista']
l1 = ''.join(l)
print(l)
print(l1)

# 2.分隔
s = '人人   都是 Pythonista'
print(s.split())
print(s.rsplit())
print(s.splitlines())

# 2.1 str.split
'''
    def split(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
        """
        S.split(sep=None, maxsplit=-1) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are
        removed from the result.(如果sep没有被指定，默认使用空格分隔，遇到多个空格，默认会当作一个空格处理)
        """
        return []
'''

print('人人    都是 pythonista'.split())  # 默认使用空格分隔，遇到多个空格，就当一个空格处理。
print('人人    都是 pythonista'.split(' '))  # 当指定了一个空格为分隔符，那么一个空格就当一个空格处理。
print('人人    都是 pythonista'.split(maxsplit=1))  # maxsplit表示从左往右分隔多少次，默认为-1，表示分隔所有分隔符。
print('人人    都是 pythonista'.split('都是'))  # 分隔符可以是任意字符串

# 2.2 str.rsplit
'''
        S.rsplit(sep=None, maxsplit=-1) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string, starting at the end of the string and
        working to the front.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified, any whitespace string
        is a separator.
'''

# rsplit就是split的翻版，split从左往右分隔，rsplit从右往左分隔。
print('人人    都是 pythonista'.rsplit(maxsplit=1))


# 自己实现split函数
def _split(s, sep, maxsplit):
    # ret 用来保存最后结果
    ret = []
    # tmp 用来保存循环字符串，直到遇到分隔符时的所有字符
    tmp = []
    i = 0
    for x in s:
        if x != sep:
            tmp.append(x)
        else:
            i += 1
            ret.append(''.join(tmp))
            tmp.clear()
        # 如果i=最大分隔数，就返回最后结果
        if i >= maxsplit and maxsplit > 0:
            return ret
    return ret


print(_split('我  爱 你', ' ', -1))


def _split2(s, sep, maxsplit):
    # ret 用来保存最后结果
    ret = []
    # tmp 用来保存循环字符串，直到遇到分隔符时的所有字符
    tmp = []
    i = 0
    for x in reversed(s):
        if x != sep:
            tmp.append(x)
        else:
            i += 1
            ret.append(''.join(reversed(tmp)))
            tmp.clear()
        # 如果i=最大分隔数，就返回最后结果
        if i >= maxsplit and maxsplit > 0:
            return reversed(ret)
    return reversed(ret)


# 2.3 str.splitlines
"""
        S.splitlines([keepends]) -> list of strings

        Return a list of the lines in S, breaking at line boundaries.
        Line breaks are not included in the resulting list unless keepends
        is given and true.
"""
s = '''哈哈
和好
嘻嘻
'''
print(s.splitlines())  # 按行分隔，且返回结果不带换行符
print(s.splitlines(True))  # 按行分隔，且返回结果带换行符

# 2.4 str.partition
'''
        S.partition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, and return the part before it,
        the separator itself, and the part after it.  If the separator is not
        found, return S and two empty strings.
        
        1.返回一个三元组 （头，分隔符，尾）
        2.按照传入的分隔符分隔一次
        3.返回的结果是head,sep,tail
'''
str = '人人\n都是\nPythonista\n哈哈'
print(str.partition(' '))
print(str.partition('\n'))
# rpartition是partition从右往左的分隔版本
print(str.rpartition('\n'))

'''通常对配置文件做操作的时候，我们会利用partition'''
cfg = 'mysql.connect = mysql://user:password@127.0.0.1:3306/test'
print(cfg.partition('='))


def _partition(s, sep):
    if s == '':
        return '', '', ''
    tmp = s.split(sep, maxsplit=1)
    if len(tmp) == 2:
        return tmp[0], sep, tmp[1]
    if len(tmp) == 1:
        return tmp[0], sep, ''
    if len(tmp) == 0:
        return '', sep, ''


'''
    总结：字符串分隔一共有5个函数， split rsplit splitlines partition rpartition
'''

# 3 大小写转换

# 3.1 upper & lower
s = 'wHc WshsF'
s2 = 'WHCC'
print(s.upper())  # 原地不修改，有返回值
print(s.lower())

# 3.2 casefold  将所有字母都转换成大小写，通常用来忽略大小写之间的比较。原地不修改，有返回值。
print(s2.casefold())

# 3.3 swapcase  大小写互换，原地不修改，有返回值。
print(s.swapcase())

# 4 排版
# 4.1 str.title  每个单词的首字母大写 原地不修改，有返回值。
print(s.title())

# 4.2 str.capitalize 一句话的首字母大写
print(s.capitalize())

# 4.3 str.center 在多少个字符中居中。
print(s.center(100))

# 4.4 str.zfill 用0补足
print(s.zfill(100))

# 5 修改

# 5.1 s.replace
s1 = '人人  人人 都是 pythonista'
print(s1.replace('人人', '每个人'))  # 返回一个新的字符串，使用new替换Old
print(s1.replace('人人', '每个人', 1))  # 可选的count参数代表替换多少次

# 5.2 s.strip
s1 = ' 哈哈 我想你  '
print(s1.strip())  # 移除字符串前后的空格
s1 = '\n\t\r 哈哈  我爱你  '
print(s1.strip())  # 其实strip移除的是空白字符
s1 = '##我#我喜#欢你 *#'
print(s1.strip('#'))  # 移除指定的字符，但仅限于前后
print(s1.strip('#我'))  # 还可以移除多个字符，按照先后书序

# 5.3 s.ljust 用来填充字符，原串在左边，若字符串大于给定的长度，不会有任何变化
print(s1.ljust(100))
print(s1.ljust(100, '$'))
print(s1.rjust(100, '@'))  # 原串在右边

# 6 查找
# 6.1 find
s = '我喜欢你很久了    '
print(s.find('我'))  # 从左往右查找，找到第一个子串，返回子串首字母的索引
print(s.find('no'))  # 当子串不存在的时候，返回-1
print(s.find('我', 1))  # start参数指定从哪里开始找
print(s.find('我', 1, -1))  # start参数指定从哪里开始找,end表示到哪里结束，-1表示最后

print(s.find(' ', 0, -1))  # 7
# 6.2 rfind  先根据start end截取字符串后,再进行查找,只是查找的顺序从右往左,截取字符串的顺序还是从左往右
print(s.rfind(' ', 0, -1))  # 9.测试

# 6.3 index
'''
    index查找，子串不存在时，抛出valueerror
    find查找，子串不存在时，返回-1
    这是index 和 find 的唯一区别
'''
# print(s.index('哈'))
print(s.index(' '))  # 7
print(s.rindex(' '))  # 10
print(s.rindex(' ', 0, -1))  # 9.测试   说明不包括最后一位

# 6.4 count  计算参数在s中的个数，当count计算的值不存在的时候返回0
print(s.count('我'))
print(s.count('我', 0, -1))  # 同样有start end参数

# 6.5 startwith  判断字符串是否以某个前缀开始，返回结果是bool值
print(s.startswith('我'))
print(s.startswith('我', 0, -1))

# 6.6 endwith  判断字符串是否以某个前缀结束，返回结果是bool值
print(s.endswith('我'))
print(s.endswith('我', 0, -1))

# 6.7 is* 字符串中有一串以is开头的方法，意思为 是否是。。
# isalnum  判断是否有字母、数字、汉子、字母的组合，其他特殊字符包括空格返回false
s = 'whc123哈哈'
print(s.isalnum())

# isdecimal 判断是否是数字
s = '123'
print(s.isdecimal())

# isidentifier 判断是否是字母或者下划线开头，且仅包含字母数字和下划线
s = 'whc5201314'
print(s.isidentifier())

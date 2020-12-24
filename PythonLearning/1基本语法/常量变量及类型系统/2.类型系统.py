# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 0:25
# @Author  : wanghc
# @File    : 2.类型系统.py
# @Software: PyCharm

# python是门强类型的动态语言，同时它又是一门解释性语言。
# 解释器语言的程序不需要在运行前编译，在运行程序的时候才编译，专门的解释器负责在每个语句执行的时候解释程序代码，这样解释型语言每执行一次就要翻译一次，效率低

# python为了避免每次执行，每次翻译，有了缓存一说。
# 执行第一次代码后，会出现一个双线划线开头双线划线结尾的文件或文件夹。
# 这里面放的是编译后的代码，下次执行如果你的代码没有改动，直接用里面的了。

# 强类型 ： 不同类型间的变量不能相互计算。

1 + 'a'  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 基本类型： int , float , bool , None

# 2内置数据结构 (built-in structure): string list tuple set dict bytes bytearray


# 动态语言： 一个变量的类型可以被多次修改、赋值
a = 4

a = 'a'

# 静态语言 ： java、C#   string  str = 'a'  一旦定义了一个变量，不能改变类型，只能改变值。

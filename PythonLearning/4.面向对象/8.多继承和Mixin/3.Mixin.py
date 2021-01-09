# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 3.Mixin.py
@time: 2021/1/9 11:53
"""


# 假设定义了三个类，都是第三方提供的，我们无法修改
class Document:
    def __init__(self, content):
        self.content = content


class Word(Document):
    def __init__(self, content):
        super().__init__('Word:{}'.format(content))


class Excel(Document):
    def __init__(self, content):
        super().__init__('Excel:{}'.format(content))


# 定义一个装饰器
def printable(cls):
    def _print(self):
        print(self)
        print(self.content)

    cls.print = _print
    return cls


@printable
class Printable(Word):
    def __init__(self, content):
        super().__init__(content)


pa = Printable('abc')
pa.print()  # <__main__.Printable object at 0x000002425BAB8700>   Word:abc

'''
如果需要新的方法，就需要在写一个装饰器。

如何解决这个问题？  另外一种方式叫做 Mixin
'''


class PrintableMixin:
    def print(self):
        print('P:{}'.format(self.content))  # 这里content哪里来并不知道


class PrintableWord(PrintableMixin, Word):
    def __init__(self, content):
        # 重写word中的__init__方法
        super().__init__(content)

'''
这里的PrintableMixin类有Print方法，Word类有content属性。
就是把其他的类的方法拿过来和另一个类的属性结合使用。 这就叫Mixin
'''
pw = PrintableWord('abc')
pw.print() # P:Word:abc

'''
Mixin类的限制：
Mixin类不该有初始化方法
Mixin类通常不能独立工作
Mixin类的祖先也应该是Mixin

通常来说Mixin类都在继承的第一位

如果Mixin有明确的继承关系，我们可以用
如果没有明确的继承关系，就可以用类装饰器

本质都是一样的，因为都是添加一些方法。

Mixin的理解：
有一个类，无法修改，我们需要扩展一些方法。
扩展的方法写在Mixin类中。

写一个类，继承Mixin类和那个无法修改的类，新的类就有要扩展的方法了。
Mixin就是用多继承来实现的，所以除了使用Mixin用多继承，其他时候不要用多继承。
'''
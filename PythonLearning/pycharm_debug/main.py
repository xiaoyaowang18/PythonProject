# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 22:22
# @Author  : wanghc
# @File    : main.py.py
# @Software: PyCharm

from PythonLearning.pycharm_debug.xxmodule import is_digit, get_xnum, get_xwords

def main():
    num1 = get_xnum()
    word = get_xwords()
    num2 = word if is_digit(word) else -1
    result = num1 + num2
    print(result)

if __name__ == '__main__':
    main()
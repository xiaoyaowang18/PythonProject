# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 22:40
# @Author  : wanghc
# @File    : 循环结构.py
# @Software: PyCharm

# while
'''
while循环需要一个条件支撑，如果条件为True，循环将继续
所以while循环内一定要有让循环退出的条件，能够改变循环条件的逻辑，否则会陷入死循环
'''
i = 0
while i < 10:
    print(i)
    i += 1

# for in 循环
'''
for关键字里实现了一个迭代协议，通过迭代协议完成了对可迭代对象的循环
可迭代对象：能用next()函数进行下一个对象的访问
'''
r = range(0, 10)
it = iter(r)
print(next(it))

for i in range(0, 10):
    print(i)

# 注意： for in 循环里不要修改可迭代对象

# 提前终止 break
# for循环里 遇到Break 将会结束本层循环，注意不是本次

for i in range(0, 10):
    if i % 2 == 0:
        print(i)
        break
        print('break')

# 如果有2个for循环，就会退出本次循环，进入上级循环的下一循环
for i in range(3):
    for j in range(5):
        print("j:" + str(j))
        if j % 2 == 0:
            print(i, j)
            break

# 跳过 continue
# 跳过本次循环，继续下一次循环（同一层）
for i in range(0, 3):
    print(i)
    if i % 2 != 0:
        continue
        print('continue')
    print(i + 1)

# else 子句
# 只有当for循环的主体循环全部结束后，才会执行else语句
# 当循环没有提前退出时，会执行else子句。

L = ['W','H','C']
for i in L:
    print(i)
else:
    print('ok')

for i in range(0,10):
    break
else:
    print('no ok')

for i in range(0,10):
    continue
else:
    print('ok')
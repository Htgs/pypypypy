#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['bbq', 'ccd', 'qqr']
for name in names:
    print(name)

# range()函数，可以生成一个整数序列
# list()函数可以转换为list
print(range(9))
print(list(range(9)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

ddd = 0
n = 99
while n > 0:
    ddd = ddd + n
    n = n % 1
print(ddd)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def area_of_circle (x):
    pi = 3.14
    return pi * x ** 2

def sum (start, end, func):
    total = 0
    for x in range(start, end):
        total += func(x)
    return total
def func1(n):
    return n

def func2(n):
    return n ** 2 + 1

print(area_of_circle(3))
print(sum(1, 100, func1))
print(sum(1, 100, func2))

print(abs(-100)) # 绝对值
print(max(99, 45, 54)) #返回最大值
print(int('1'))
print(float('1.32'))
print(str(1.32))
print(bool(1.32))

# 空函数
def function():
    pass

# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# 两者错误不同
# print(my_abs('A'))
# print(abs('A'))

def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# print(my_abs('A'))
# print(abs('A'))

import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, math.pi/6, 90)
r = move(100, 100, math.pi/6, 90)
# 返回多个值，其实是一个tuple
print(x, y)
print(r)
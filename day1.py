#!/usr/bin/env python
# -*- coding: utf-8 -*-


# py 3+ 必须用print()
print ('who are you')

# py3没有这个 raw_input() 它把所有的输入都直接当作一串字符，于是就可以不用加引号
# raw_input()
# 输入方法
input()


print ('oo')



string = 'string'

number = 666

boolean = True

floats = 6.666

print (string)
print (number)
print (boolean)
print (floats)

# >：大于
# <：小于
# >=：大于等于
# <=：小于等于
# ==：等于。比较两个值是否相等。之所以用两个等号，是为了和变量赋值区分开来。
# !=：不等与
# not：逻辑“非”。如果x为True，则not x为False
# and：逻辑“与”。如果x为True，且y为True，则x and y为True
# or：逻辑“或”。如果x、y中至少有一个为True，则x or y为True


a = True
b = not a  #不记得not请回复6

print (b) #f
print (not b) #t
print (a == b) #f
print (a != b) #t
print (a and b) #f
print (a or b) #t
print (1<2 and b==True) #f

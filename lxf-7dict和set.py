#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict 使用键-值（key-value）存储，具有极快的查找速度
d = {'qqq': 1, 'bbb': 2, 'ccc': 3}
print(d['qqq']) # 1

# 通过in判断key是否存在
print('db' in d) # False
print('qqq' in d) # True

#通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
# !!!返回None的时候Python的交互式命令行不显示结果
print(d.get('qqq', -1)) # 1
print(d.get('ppp')) # None 
print(d.get('ddd', -1)) # -1

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(d.pop('bbb'))
print(d)

# !!!和list比较，dict有以下几个特点：
# dict ↓
# !!!查找和插入的速度极快，不会随着key的增加而变慢；
# !!!需要占用大量的内存，内存浪费多。
# list ↓
# !!!查找和插入的时间随着元素的增加而增加；
# !!!占用空间小，浪费内存很少。



# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
s = set([111, 111, 2333])
print(s) # {2333, 111}
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add('ddd')
print(s) # {'ddd', 2333, 111}
# 通过remove(key)方法可以删除元素
s.remove(111) 
print(s) # {2333, 'ddd'}

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2) # {2, 3}
print(s1 | s2) # {1, 2, 3, 4}

# !!!str是不变对象，而list是可变对象
a = ['c', 'b', 'a']
a.sort()
print(a) # ['a', 'b', 'c']

stra = 'abc'
strb = stra.replace('a', 'A')
print(stra) # 'abc'
print(strb) # 'Abc'
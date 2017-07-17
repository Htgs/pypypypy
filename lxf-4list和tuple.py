#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
lists = ['pp', 'qq', 'se']
print(len(lists))
print(lists[-1]) # 获取最后一个元素
print(list)

# append() list中追加元素到末尾
lists.append('dd')
print(lists)

# insert(index, element) 把元素插入到指定的位置，比如索引号为1的位置
lists.insert(1, 'jdail')
print(lists)

# pop() 删除list末尾的元素
lists.pop()
print(lists)

# 元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
tuples = ('aa', 'bb', 'cc')
print(tuples)
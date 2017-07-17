#!/usr/bin/env python3
# -*- coding: utf-8 -*-

tuples1 = (1, 2, 3)
tuples2 = (1, [2, 3])
d = {'aa': tuples1, 'bb': tuples2}
# s = set([tuples1, tuples2]) 会报错
print(d)
# print(s)
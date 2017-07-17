print('\\\t\\')
#r'' 不转义
print(r'\\\t\\')

print('''line1
line2
line3''')

print(True)
print(False)
print(True and False)
print(True or False)
print(not False)

#空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
print(None == 0) # False

a = 'ABC'
b = a
a = 'XZY'
print(b) # 'ABC'

print(10/3) # 3.3333333333333335
print(9/3) #3.0
# 整数的地板除//永远是整数，即使除不尽。要做精确的除法，使用/就可以
print(10//3) #3
print(10%3) #1
# Ways to create arrays in numpy
# array()
# linspace()
# logspace()
# arange()
# zeros()
# ones()

from numpy import *

arr = array([1,2,3,4,5])
print(arr)
print(arr.dtype)

print('====================')

arr = array([1,2,3,4,5.2])
print(arr)
print(arr.dtype)

print('====================')

arr = array([1,2,3,4,5], int)
print(arr)
print(arr.dtype)

print('====================')

arr = array([1,2,3,4,5], float)
print(arr)
print(arr.dtype)

print('====================')

arr = linspace(0, 9, 10)
print(arr)

print('====================')

arr = linspace(1, 16, 4)
print(arr)

print('====================')

arr = linspace(0, 10)
print(arr)
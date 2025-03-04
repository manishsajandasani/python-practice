# Array is similar to List
# There is only one difference i.e. an array can contain elements of same data-type
# Ex: integer array, string array, etc. 
# Array can contain any number of elements
# We can shrink or expand the size of an array in python 
# Learn all these typecodes i, I, u, f, d (to create a specific data type array)

from array import *

# print('====================')
# vals = array('I', [2, -3, 80, 5])
# print(vals)

# print('====================')
# vals = array('i', [2, 3.5, 80, 5])
# print(vals)

vals = array('i', [2, 3, 80, -5, 56])
print(vals)
print(vals.buffer_info())
print(vals.typecode)
vals.append(10)
print(vals)
vals.reverse()
print(vals)
print(vals[0])

print('=======================')

for i in range(len(vals)):
  print(vals[i])

print('=======================')

for i in vals:
  print(i)

print('=======================')

for c in array('u', ['A', 'B', 'C', 'D', 'E']):
  print(c)

print('=======================')
print('Copying an array to another array')
arr_1 = array('i', [1,2,3,4,5])
arr_2 = array(arr_1.typecode, (a for a in arr_1))
for a in arr_2:
  print(a)
  
print('=======================')
arr_3 = array(arr_1.typecode, (a*a for a in arr_1))
for a in arr_3:
  print(a)

print('=======================')
arr_3 = array(arr_1.typecode, (a*a for a in arr_1))
for a in arr_3:
  print(a)

print('=======================')
i = 0
arr_4 = array('i', [])
while(i < len(arr_3)):
  arr_4.append(arr_3[i] * 4)
  i+=1
print(arr_4)

from array import *

arr = array('i', [])
n = int(input('Enter the length of the array: '))

for i in range(n):
  x = int(input('Enter the next value: '))
  arr.append(x)

print(arr)

val = int(input('Enter the value for search: '))

k = 0
for e in arr:
  if e == val:
    print(f'Manual Way: The index of {val} is {k}')
    break
  k+=1
else:
  print('Value not found')

print(f'In-Built Function: The index of {val} is {arr.index(val)}')

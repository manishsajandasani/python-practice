# In order to use for-else, we must be having a condition with break statement inside the for loop. The for-else part would run if the for loop's condition never breaks

nums = [10, 12, 18, 21, 26]
# nums = [11, 12, 18, 21, 26]

for num in nums:
  if(num%5 == 0):
    print(num)
    break
  # else:
  #   print('not found')
else:
  print('not found')
if True:
  print('I am right')
else:
  print('I am wrong')

print('\n================\n')

x = 6
r = x % 2
if r==0:
  print('Even')
  if(x > 5):
    print('Greater than 5')
  else:
    print('Lesser than 5')
else: 
  print('Odd')

print('Bye')

print('\n================\n')

day = 8

if(day == 1):
  print('Sunday')
elif (day == 2):
  print('Monday')
elif (day == 3):
  print('Tuesday')
elif (day == 4):
  print('Wednesday')
elif (day == 5):
  print('Thursday')
elif (day == 6):
  print('Friday')
elif (day == 7):
  print('Saturday')
else:
  print('Wrong Input')

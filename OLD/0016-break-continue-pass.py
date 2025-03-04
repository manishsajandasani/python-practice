av = 3
x = int(input('How many candies you want?'))

i = 1
while(i <= x):
  if(i > av):
    print('Out of Stock')
    break
  print('Candy')
  i+=1

print('Bye')

print('=========================')

for i in range(1, 31):
  if(i%5 == 0 or i%3 == 0):
    continue
  print(i)  

print('=========================')

for i in range(1, 31):
  if(i%2 == 0):
    # I don't know what to do here & for time being just pass
    pass
  else:
    print(i) 
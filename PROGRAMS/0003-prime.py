# for j in range(2, 11):
#   count = 0
#   for i in range(2, j):
#     if j%i == 0:
#       count+=1
#   if count==0:
#     print(f"{j} is a prime number")
#   else:
#     print(f"{j}")

# print('=======================')

num = 31 
for j in range(2, num):
  if num%j == 0:
    print(f"{num} is not a prime number")
    break
else:
  print(f"{num} is a prime number")


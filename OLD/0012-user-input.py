# input function always give you a string value

# x = input('Enter first number \n')
# y = input('Enter second number \n')
# print(x + y)
# print(type(x), type(y))
# print(int(x) + int(y))

# name1 = input('Enter your name')
# print(name1[0])
# name2 = input('Enter your name')[0]
# print(name2)

# To evaluate the whole expression, use eval function
# exp = eval(input('Enter an expression'))
# print(exp)

# We can accept arguments from command line as well
# In command line write below:
# python 0012-user-input.py 5 10
# here index of 0012-user-input.py is 0
# here index of 5 is 1
# here index of 10 is 2

import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
print(a + b)
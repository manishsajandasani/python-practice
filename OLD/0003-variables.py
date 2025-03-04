x = 2
print(3 + x)

y = 10
print(x ** y)
# print(_ + 10)    # not working here. Find meaning of _

name = 'Manish'
print('My name is ' + name)
print(name[0])
print(name[-1])
print(name[-6])

platform = 'Youtube'
print(platform[1:4])
print(platform[1:])
print(platform[:2])
print(platform[1:50])

print('My ' + platform[3:])

# Strings in Python are Immutable
# TypeError: 'str' object does not support item assignment

platform[0] = 'T'

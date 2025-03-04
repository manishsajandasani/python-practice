a = 10
b = a
print(id(a))
print(id(b))
c = 10
print(id(c))

a = 11
print(id(a))
print(id(b))

aa = 'Manish'
bb = 26
cc = 30.45
print(type(aa))
print(type(bb))
print(type(cc))

hobbies = ['A', 'B', 'C']
print(type(hobbies))

student = {'id' : 1, 'name' : 'Manish', 'hobbies' : ['Cricket', 'Football']}
print(type(student))

# There is a concept of constant which is not present in Python but we can create it by showing our intentions. We just create the variable in UPPERCASE

# Here PI is a regular variable. However, it is in uppercase so we are considering it as an Constant
PI = 3.14
print(type(PI))
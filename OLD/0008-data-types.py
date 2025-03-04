# Data Types
# None
# Numeric 
    # int
    # float
    # complex
    # bool
# Sequence 
    # List
    # Tuple
    # Set
    # String
    # Range
# Mapping
    # Dictionary

num = 2.5
print(type(num))
num = 5
print(type(num))
num = 5 + 2j
print(type(num))
num = True
print(type(num))

a = 5.6
b = int(a)
print(a, b)
print(type(a), type(b))

c = float(b)
print(c, type(c))

d = 10
e = 11
f = complex(d,e)
print(f, type(f))

bool = d<e
print(bool, type(bool))
bool = d>e
print(bool, type(bool))
bool = int(True)
print(bool, type(bool))
bool = int(False)
print(bool, type(bool))

hobbies = ['A', 'B', 'C']
print(type(hobbies))

s = {98, 56, 98, 15, 19}
print(s, type(s))

t = (15, 18, 'Manish', 56)
print(t, type(t))

student = {'id' : 1, 'name' : 'Rohan', 'hobbies' : ['Cricket', 'Football']}
print(student, type(student))
print(student['name'], type(student['name']))
print(student.get('id'), type(student['id']))

str = 'Manish'
print(str, type(str))

st = 'M'
print(st, type(st))

r = range(10)
print(r, type(r))
r = list(range(10))
print(r, type(r))
r = list(range(4, 11, 2))
print(r, type(r))


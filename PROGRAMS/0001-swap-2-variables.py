# With third variable
a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)

# Without third variable
c = 11
d = 12
c = c + d
d = c - d
c = c - d
print(c, d)

# With XOR
e = 21
f = 22
e = e ^ f
f = e ^ f
e = e ^ f
print(e, f)

# Only in Python
g = 31
h = 32
g, h = h, g 
print(g, h)

# Tuple is List. Difference: List (Mutable) and Tuple (Immutable)
# Tuple is used when we know we aren't going to change the values.
# Iteration in Tuple is fast than List

tup = (2,1,2,3,2,4,2)
print(tup)
print(tup[1])

# TypeError: 'tuple' object does not support item assignment
# tup[2] = 5
# print(tup)

print(tup.count(2))
print(tup.index(4))


# Set is a collection of Unique Elements
# Set doesn't give values in a specific order
# Set uses Hash Technique to return the elements
# Set doesn't peform ordering by default
# Set doesn't have an order so we can't use indexing
# Set doesn't support duplicated values and doesn't maintain sequence
# It is almost same as List

myset = {98,14,5,100,78,52,98}
print(myset) 



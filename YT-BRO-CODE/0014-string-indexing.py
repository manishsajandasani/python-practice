# String indexing is accessing elements of a sequence using [] (indexing operator)
# [start : end : step]  

credit_number = "1234-5678-9012-3456"

print(f"Index 0 value = {credit_number[7]}")
print(f"First 4 digits = {credit_number[0:4]}")
print(f"Next 4 digits = {credit_number[5:9]}")
print(f"From 5 digit till end = {credit_number[5:]}")
print(f"last index value = {credit_number[-1]}")
print(f"last 2nd value = {credit_number[-2]}")
print(f"last 3rd value = {credit_number[-3]}")
print(f"Entire string = {credit_number[::]}")
print(f"Prints every second character = {credit_number[::2]}")
print(f"Last 4 digits = {credit_number[-4:]}")
print(f"Reverse the string = {credit_number[::-1]}")
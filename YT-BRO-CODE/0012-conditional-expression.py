"""
    Conditional expression is a one-line shortcut for the if-else statement (ternary operator)
    Print or assign one of two values based on a condtion
    X if condition else Y
"""

# num = -5
# print("Positive" if num > 0 else "Negative")

# num = 11
# print("EVEN" if num % 2 == 0 else "ODD")

# a = 10
# b = 17
# print(a if a > b else b)

# age = 15
# print("Adult" if age >= 18 else "Child")

user_role = "guest"
print("Full Access" if user_role == "admin" else "Limited Access")

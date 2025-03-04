# String Methods
# len(), x.find(...), x.rfind(...), x.capitalize(), x.upper(), x.lower(), x.isdigit(), x.isalpha()
# x.count(...), x.replace(..., ...)

# name = input("Enter your full name: ")
# print(f"Length of name is {len(name)}")
# print(f"find (First Occurence): {name.find(" ")}")
# print(f"find (First Occurence): {name.find("o")}")
# print(f"rfind (Last Occurence): {name.rfind("o")}")
# print(f"capitalize first letter: {name} => {name.capitalize()}")
# print(f"uppercase: {name} => {name.upper()}")
# print(f"lowercase: {name} => {name.lower()}")
# print(f"isdigit: {name.isdigit()}")
# print(f"isalpha: {name.isalpha()}")

# ==================================================================================
# ==================================================================================

# phone = input("Enter your phone number: ")
# dashCount = phone.count("-")
# print(dashCount)
# replaceDash = phone.replace("-", "=>")
# print(replaceDash)
# print(phone)

# ==================================================================================
# ==================================================================================

# print(help(str))

# ==================================================================================
# ==================================================================================

# Validate User Input Exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your name: ")

if len(username) > 12:
    print('username can not be more than 12 characters')
elif not username.find(" ") == -1:
    print('username must not contain spaces')
elif username.isdigit():
    print('username must not contain digits')
else:
    print('username is valid')

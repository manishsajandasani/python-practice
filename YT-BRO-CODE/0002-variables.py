# Variables
# A container for a value (string, integer, float, boolean)
# A variable behaves as if it was the value it contains
# f-string - ?? (Get the definition)

#  Strings - Series of characters
first_name = "Manish"
print(first_name)
print(f"Hello {first_name}")

food = "Pani Puri"
print(f"You like {food}")

email = "sajan@gmail.com"
print(f"You're email is {email}")

# ==================================================================================
# ==================================================================================

# Integers - Whole Numbers
age = 32
print(f"You are {age} years old")

quantity = 3
print(f"You are buying {quantity} items")

num_of_students = 30
print(f"Your class has {num_of_students} students")

# ==================================================================================
# ==================================================================================

# Float - With Decimal
price = 10.99
print(f"The price if ${price}")

gpa = 3.2
print(f"Your GPA is ${gpa}")

distance = 5.5
print(f"You ran ${distance} kilometers")

# ==================================================================================
# ==================================================================================

# Boolean
is_student = False
for_sale = False
is_online = True

if is_student:
    print("You are a student")
else:
    print("You are not a student")

print(f"Is this car for sale? {for_sale}")
print(f"Is your friend online? {is_online}")

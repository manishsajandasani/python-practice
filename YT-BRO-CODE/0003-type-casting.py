# Type Casting is the process of converting a value of one data type to another
# Types are Explicit Type Casting and Implicit Type Casting

name = "Manish"
age = 32
gpa = 8.9
student = True

variables = [name, age, gpa, student]
for variable in variables:
    print(type(variable))

# Integer to Float (Explicit Type Casting)
age = float(age)
print(f"Age is now float {age}")

# Float to Integer (Explicit Type Casting)
gpa = int(gpa)
print(f"gpa is now integer {gpa}")

# Boolean to String (Explicit Type Casting)
student = str(student)
print(f"student is now string {student}")
print(f"Type of student is {type(student)}")

# Cast to Boolean (Explicit Type Casting)
print(f"Any random number - {bool(age)}")
print(f"Any negative number - {bool(-1)}")
print(f"Zero - {bool(0)}")
print(f"Any string - {bool('Manish')}")
print(f"Empty string - {bool('')}")
print(f"Space - {bool(' ')}")
print(f"Empty list - {bool([])}")
print(f"List - {bool([1, 'Hello'])}")

# ==================================================================================
# ==================================================================================

# Implicit Type Casting
x = 2
y = 2.0
x = x / y
print(x)

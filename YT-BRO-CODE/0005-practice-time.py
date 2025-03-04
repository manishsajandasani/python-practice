# Exercise 1 : Mad Libs
noun = input('Enter a noun: ')
verb = input('Enter a verb: ')
adjective1 = input('Enter first adjective: ')
adjective2 = input('Enter second adjective: ')
adjective3 = input('Enter third adjective: ')

print(f"Today I went to a {adjective1} zoo")
print(f"In an exhibit, I saw a {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")

# ==================================================================================
# ==================================================================================

# Exercise 2 : Calculate area of rectangle
length = float(input("Enter the length of a rectange: "))
width = float(input("Enter the width of a rectange: "))
print(f"Area of rectangle (l={length} & w={width}) is {(length * width)}cm^2")

# ==================================================================================
# ==================================================================================

# Exercise 3 : Shopping Cart
item = input("What item would you like to buy? ")
price = float(input("What is the price? "))
quantity = int(input("How many would you like? "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${round(total, 2)}")

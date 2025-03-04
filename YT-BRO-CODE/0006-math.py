# friends = 15
# friends = friends + 1
# friends += 1
# friends = friends - 1
# friends -= 1
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# friends = friends % 7
# friends %= 3
# print(friends)

# ==================================================================================
# ==================================================================================

# Some useful built-in Math functions
# x = 3.165
# y = -4
# z = 5
# print(round(x))
# print(round(x, 1))
# print(round(x, 2))
# print(pow(z, 3))
# print(max(x, y, z))
# print(min(x, y, z))

# ==================================================================================
# ==================================================================================

# Math class constants and functions
import math

print(math.pi)
print(math.e)
print(math.sqrt(4))
print(math.sqrt(5))
print(math.floor(8.1))
print(math.ceil(8.1))
print(math.floor(8.6))
print(math.ceil(8.6))

print(f"Circumference of a circle {round(2 * math.pi * 49, 2)}cm")
print(f"Area of a circle {round(math.pi * math.pow(10.5, 2), 2)}cm^2")
print(f"Square root of a^2 + b^2 is {math.sqrt(pow(10, 2) + pow(11, 2))}")

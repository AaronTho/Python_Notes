import math


loss = -20.25
product_cost = 89.99

print(abs(loss))

print(math.floor(product_cost))  # Rounds down to the nearest whole number
print(math.ceil(product_cost))  # Rounds up to the nearest whole number
print(abs(math.floor(loss)))
print(round(product_cost))  # Rounds to the nearest whole number
print(math.sqrt(product_cost))
# Finds the square root. Equal to (5 ** 2) but math.pow is far more accurate for complex calculations
print(math.pow(5466, 3))
print(5466 ** 3)

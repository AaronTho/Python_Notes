sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    1,
    3
]

# Sort changes the structure of the list
sale_prices.sort()

# Sorted can be saved in a new variable, but will not change the original list
sorted_list = sorted(sale_prices)
sorted_list = sorted(sale_prices, reverse=True)
print(sorted_list)

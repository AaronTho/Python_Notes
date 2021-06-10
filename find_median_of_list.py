import math

sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]

# My Solution

sorted_sale_prices = sorted(sale_prices)
length_of_sale_prices = len(sorted_sale_prices)
half_price_list = length_of_sale_prices // 2
median_number = sorted_sale_prices[half_price_list]

print(sorted_sale_prices)
print(median_number)


# Bottega's Worse Solution

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)

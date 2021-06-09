api_data = '5'
greeting = 'Hi'

print(api_data.isalpha())
print(greeting.isalpha())
# Returns boolean response. Spaces are NOT alphanumeric. So using .isnumeric is more reliable.

print(api_data.isnumeric())
print(greeting.isnumeric())

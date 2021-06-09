name = 'Kristine'
age = 12
product = 'Python eLearning course'

greeting = 'Hi {0}, you are listed as {1} years old and you have purchased: {2}'.format(
    name, age, product)

# You can use the assigned elements in any order as long as they are mapped in order. But you need to use all of the mapped arguments.

print(greeting)

# String Literal method:

next_greeting = f'Hi {name}, you are listed as {age} years old and you have purchased: {product}.'

print(next_greeting)

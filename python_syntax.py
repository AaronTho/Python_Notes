# name = input('What is your name? ')
# color =input('What is your favorite color? ')
# print(name + ' likes ' + color + '.')

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2021 - int(birth_year)
# print(type(age))
# print(age)

# weight = input('What is your weight? ')
# kilo_weight = int(weight) * .453592
# print(str(kilo_weight) + ' kg')

# course = "Python's Course for Beginners"
# print(course)

# course = 'Python\'s Course for "Beginners"'
# print(course)

# course + '''
# What's up, dude?
# I found your mom at Walmart.
# '''
# print(course)

# course = 'Python for Beginners'
# another = course[:]
# print(course)


# name = "Jennifer"
# print(name[1:-1])

# first = 'john'
# last = 'smith'
# message = first + ' [' + last + '] is a coder.'
# msg = f'{first} [{last}] is a coder.'
# print(msg)

# course = 'Python for Beginners'
# print('Python' in course)

# print(course.replace('Beginners', 'Absolute Beginners'))

# print(course.upper())
# print(course.lower())


# print(10 + 3)
# print(10 // 3)

# x = 2.9
# print(round(x))
#

house_price = 1000000
credit_good = False
credit_bad = True

if credit_good:
    down_payment = house_price * .10
elif credit_bad:
    down_payment = house_price * .20

print(down_payment)

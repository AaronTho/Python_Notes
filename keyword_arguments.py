def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print('Start')
greet_user(last_name='Smith', first_name='John')
print('Finish')

# When mixing positiontal and keyword arugments, place the positional arguments first.
# Numerical arguments which are not clear should use keyword arugments to make your code more clear.

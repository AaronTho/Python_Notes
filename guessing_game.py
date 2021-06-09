# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('Winner winner chicken dinner!')
#         break
#     elif guess_count == guess_limit and guess == secret_number:
#         print('Winner winner chicken dinner!')
#     elif guess_count == guess_limit:
#         print('Out of tries!')
#         break
#     else:
#         print('Try again!')


# New version with random number generator...
import random

for i in range(1):
    x = (random.randint(1, 10))


secret_number = x


def secret_number_print():
    print(f'Sorry, you lost. The correct answer was {secret_number_print}.')


guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('Winner winner chicken dinner!')
        break
    if guess != secret_number:
        print('Nope, try again!')
    if guess == 'help':
        print('The answer is a number between 1-10. You have three guesses, and you look really nice today.')
else:
    print(f'Sorry, you lost. The correct answer was {secret_number}.')

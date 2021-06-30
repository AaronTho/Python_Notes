# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1
# print('Done')

# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print('Done')

nums = list(range(1, 100))

while len(nums) > 0:
    print(nums.pop())


def guessing_game():
    while True:
        print('What is your guess?')
        guess = input()

        if guess == '42':
            print('You correctly guessed it!')
            return False
        else:
            print(f"No, {guess} isn't the answer, please try again\n")


guessing_game()

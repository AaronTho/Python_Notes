# temperature = 80

# if temperature > 80:
#     print("It's a hot day, Bubba.")
# else:
#     print("It's not a hot day, Bubba.")


name = input("Name: ")

# name_length = len(name) -Don't need a new variable here
if len(name) < 3:
    print('Name must be at least 3 characters long.')
elif len(name) > 50:
    print('Name must be less than 50 characters long, you weirdo.')
else:
    print('Nice name. You have a sister?')

# guess_count = 0
# guess_limit = 300

# while guess_count < guess_limit:
#     guess = input('>').lower()
#     guess_count += 1
#     if guess == 'start':
#         print('Car started...Ready to go!')
#     elif guess == 'stop':
#         print('Car stopped.')
#     elif guess == 'quit':
#         break
#     elif command == "help":
#         print("""
#             start - to start the car
#             stop - to sto the car
#             quit - to quit
#             """)
#     elif guess != 'start':
#         print("I don't understand that...")

started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car is already started, you muppet!')
        else:
            started = True
            print('Gentlemen, your engines are started!')
    elif command == 'stop':
        if not started:
            print("Car is already stopped, Lady Broseph!")
        else:
            started = False
            print('Car stopped.')

    elif command == "help":
        print("""
start - to start the car
stop - to sto the car
quit - to quit
        """)
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that...")

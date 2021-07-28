print('Welcome to my quiz!')

playing = input('Do you wan to play? ')

if playing.lower() != 'yes':
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does GPU stand for? ")

if answer.lower() == 'graphics processing unit':
    print('Correct!')
    score += 1
else:
    print('Sorry, but you are very dumb. Our data suggests your mother smoked a lot.')

answer = input("What does RAM stand for? ")

if answer.lower() == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Sorry, but you are very dumb. Our data suggests your mother smoked a lot.')

answer = input("What does PSU stand for? ")

if answer.lower() == 'power supply unit':
    print('Correct!')
    score += 1
else:
    print('Sorry, but you are very dumb. Our data suggests your mother smoked a lot.')

answer = input("What does LDS stand for? ")

if answer.lower() == 'latter day saint':
    print('Correct!')
    score += 1
else:
    print('Sorry, but you are very dumb. Our data suggests your mother smoked and was indifferent towards you.')

print("You got " + str((score / 4) * 100) + "%.")

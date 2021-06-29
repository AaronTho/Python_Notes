players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

for player in players:
    print(player)

players = {
    '2b': 'Altuve',
    '3b': 'Bregman',
    'ss': 'Correa',
    'dh': 'Gattis'
}

for position, player in players.items():
    print('Position', position)
    print('Player', player)


alphabet = 'abcdef'

for letter in alphabet:
    print(letter)


for num in range(1, 10):
    print(num)

for num in range(1, 10, 2):
    print(num)

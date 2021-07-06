"""

full_name = lambda first, last: f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens'))
"""


def lambda_practice(first): return f'{first}'


def greeting(name):
    print(f'Hi, {name}')


greeting(lambda_practice('Jordan'))

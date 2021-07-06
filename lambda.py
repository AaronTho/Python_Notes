"""

full_name = lambda first, last: f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens'))
"""


def greeting(name): return f'Hi, {name}'


print(greeting('Jordan'))
# greeting(lambda_practice('Jordan'))

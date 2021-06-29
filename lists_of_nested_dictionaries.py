teams = [
    'My String',
    {
        'astros': {
            '2B': 'Altuve',
            'SS': 'Correa',
            '3B': 'Bregman',
        }
    },
    {
        'angels': {
            'OF': 'Trout',
            'DH': 'Pujols',
            'LFP': 'Romo',
        }
    }
]

# print(teams[0])

angels = teams[1].get('angels', 'Team not found')

# print(list(angels.values())[1])

teams_index = teams.index('My String')

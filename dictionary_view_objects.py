players = {
    "ss": "Correa",
    "2b": "Altuve",
    "3b": "Bregmans",
    "DH": "Gattis",
    "OF": "Springer",

}

# print(players.items())
# print(players.values())
# print(players.keys())
# Returns: a view of the items, values, keys in the dictionaires in tuples.

# print(list(players.values())[1])
# Returns: Altuve

# print(list(players.copy().values()))
# Returns a copy of the values at that moment which will not be dynamic

teams = {
    "astros": ["Altuve", "Corea", "Bregman"],
    "giants": ["Pence", "Posey", "Austin", "Dugger"],
    "angels": ["Trout", "Pujols", ['Thompson', 'Smith']],
    "yankees": ['Judge', 'Stanton'],
}

team_groupings = teams.items()
print(list(team_groupings)[2][1][2][1])
# Returns: Smith

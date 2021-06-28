teams = {
    "astros": ["Altuve", "Corea", "Bregman"],
    "giants": ["Pence", "Posey", "Austin", "Dugger"],
    "angels": ["Trout", "Pujols", ['Thompson', 'Smith']],
    "yankees": ['Judge', 'Stanton'],
}

removed_teams = teams.pop('astros', 'No team found by that name')

print(removed_teams)

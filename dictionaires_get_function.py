teams = {
    "astros": ["Altuve", "Corea", "Bregman"],
    "giants": ["Pence", "Posey", "Austin", "Dugger"],
    "angels": ["Trout", "Pujols"],
    'yankees': ['Judge', 'Stanton'],
}

featured_team = teams.get('mets', 'No featured team')
# Creates a fallback response insteat of throwing an error

print(featured_team)
# Returns KeyError 'mets' because 'mets' is not in the dictionary.

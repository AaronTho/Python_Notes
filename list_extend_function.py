tags = [
    'python',
    'development',
    'tutorials',
    'code',
]

# Nope

tags[-1] = 'Programing'

# In place
tags.extend("Programming")

new_tags = tags.append('Programming')

# New List
tags.extend(["Programming"])

new_tags = tags + ['Programming']

print(new_tags)

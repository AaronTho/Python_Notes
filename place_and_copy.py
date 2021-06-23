tags = ['python', 'development', 'tutorials', 'code']

tags.extend('Programming')
# Returns: ['python', 'development', 'tutorials', 'code', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']

new_tags = tags.extend(['Programming'])
# Returns: None

new_tags = tags + ['Programming']
print(tags)

tags.append('Programming')
print(tags)

backwards_tags = tags[::-1]
print(backwards_tags)

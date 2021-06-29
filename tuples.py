# numbers = (1, 2, 3)
# numbers[0] = 10  # returns an error because tuples are immutable.

"""
only the .count and .index methods work on tuples
"""

# list: [] mutable
# Dictionary: {}
# Tuple: () immutable

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

title, sub_heading, content = post

# If you run a .sort function on this as a list the unpacking will no longer work. But you cannot sort a tuple.

# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)
print(sub_heading)
print(content)

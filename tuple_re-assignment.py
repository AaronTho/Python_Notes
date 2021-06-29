post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))
print(id(post))
post += ('published',)
# post = post + ('published',) == post += ('published',)

print(id(post))

# This id print will return a new number because we have created a new object in memory by adding 'published'.

# You MUST add the comma to the item you are adding to the tuple.

# title, sub_heading, content, status = post

# print(title)
# print(sub_heading)
# print(content)
# print(status)

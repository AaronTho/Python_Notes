post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

tuple_list = ['My Name', 'Akira', 'Your Lie In April']
post += (tuple_list,)
# Do not forget the comma.

print(post)

print(post[-1][1])
# Returns: 'Akira'

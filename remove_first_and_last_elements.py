html = ['<h2>', 'Some content', '</h1>']

html2 = ['<h1>', "Some content", 'more', 'even more', '</h1>']

list_of_ints = [1, 5, 7, 8, 9, 3, 5, 7]


def remove_first_and_last(list_to_clean):
    _, *content, _, _ = list_to_clean
    return content


print(remove_first_and_last(list_of_ints))

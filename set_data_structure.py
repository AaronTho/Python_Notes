# Uniqueness
tags = {
    'python',
    'coding',
    'tutorials',
    'coding'
}

# Sets use {} without key value pairs. All items in a set MUST be unique. Repeated elemts will not be returned.

print(tags)

# Nope. Set objects do not support indexing.
# print(tags[0])

query_one = 'python' in tags
query_two = 'ruby' in tags
# Will return a True/False boolean.

print(query_one)
print(query_two)

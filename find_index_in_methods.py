sentence = 'The quick brown fox jumped over the lazy dog.'

# Throws a -1 if it cannot find the value.
quary = sentence.find('quick')
# Will throw an error if it cannot find the value.
quary_two = sentence.index('quick')


print(quary)  # Returns the index location of 'quick'.
print(quary)

# The in method will return a boolean. Does the sentence contain the substring or not?
query_three = 'fox' in sentence
query_four = 'oops' in sentence

print(query_three)
print(query_four)

numbers = [5, 2, 1, 7, 4]
numbers.clear()  # removes all items from list
numbers.append(20)  # adds to the end of the list
numbers.insert(0, 10)  # inserts list at location
numbers.remove(5)  # removes item from list
numbers.pop()  # remove last item form list
# returns the index location of the first occurance of the specified element
numbers.index(5)
# returns a boolean value for the existence of an item in a list
print(50 in numbers)
print(numbers.count(5))  # returns the number of occurances of an item in a list
numbers.sort()  # orders the list numerically
numbers.reverse()  # reverses the sort order
# create a copy of the list which will not be altered by any subsequence modifiers
numbers2 = numbers.copy()

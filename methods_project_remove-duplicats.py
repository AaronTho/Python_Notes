numbers = [1, 2, 3, 4, 4, 4, 5, 6]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

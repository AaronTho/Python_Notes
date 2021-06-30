def loop_using_while():
    dog_house = ['red', 'pat', 'rover', 'sushi']
    counter = 0
    while counter < 4:
        print(dog_house[counter])
        counter += 1

    return [dog_house, counter]


loop_using_while()

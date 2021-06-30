def loop_over_list():
    numbers = [1, 2, 3, 4, 5, 6]
    result = []

    for number in numbers:
        result += numbers
        # numbers.append(result)

    return result


loop_over_list()

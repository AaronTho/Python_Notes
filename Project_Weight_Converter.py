weight = input('Weight: ')
unit_of_weight = input('(L)bs or (K)g: ')

if unit_of_weight.upper() == 'L':
    result = float(weight) * 0.453592
    print(f'You weigh {result} kg.')
elif unit_of_weight.upper() == 'K':
    result = float(weight) * 2.20462
    print(f'You weigh {result} lbs.')

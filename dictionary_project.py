phone_number = input("Phone: ")

number_words = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '-': '-',

}
output = ''
for digits in phone_number:
    output = output + number_words.get(digits,  "!") + ' '
print(output)

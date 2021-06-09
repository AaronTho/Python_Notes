# has_high_income = True
# has_good_credit = True

# if has_good_credit and has_high_income:
#     print('Eligible for loan.')

# has_high_income = True
# has_good_credit = False

# if has_good_credit or has_high_income:
#     print('Eligible for loan.')
# else:
#     print('Not eligble for loan.')

has_criminal_record = False
has_good_credit = True

if has_good_credit and not has_criminal_record:
    print('Eligible for loan.')
else:
    print('Not eligble for loan.')

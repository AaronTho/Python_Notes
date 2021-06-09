try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)

except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print('Inavlid value')


# Exit code 0 means there were no erros.
# exit code anything but 0 means our program crashed.
# Try - Except blocks prevent program crashing errors.

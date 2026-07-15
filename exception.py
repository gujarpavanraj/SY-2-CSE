class NegativeNumberError(Exception):
    pass

num = int(input("Enter a number: "))

try:
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    else:
        print("You entered:", num)

except NegativeNumberError as e:
    print(e)
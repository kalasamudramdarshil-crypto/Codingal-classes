try:
    number = int(input('Enter a number: '))
    print("This number is", number)

except ValueError as ve:
    print(ve)
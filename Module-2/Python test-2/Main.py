def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b 
def divide(a,b):
    return a / b

print("Calculator")
print("Enter a number of your choice"(1,2,3,4))

try:
    choice = input("Enter operation (+, -, *, /):")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '+': print("Result:", add(num1, num2))
    elif choice == '-': print("Result:", subtract(num1, num2))
    elif choice == '*': print("Result:", multiply(num1,num2))
    elif choice == '/': print("Result:", divide(num1,num2))
    else: print("Invalid operation")

except ValueError: 
    print("Error: Please enter numbers only")
except ZeroDivisionError:
    print("Error: You cannot do division by zero")
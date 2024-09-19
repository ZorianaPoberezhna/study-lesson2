try:
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    print(f"You entered the numbers: {num1}, {num2}")
except ValueError:
    print("Error. Enter correct numbers!")

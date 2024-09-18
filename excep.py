def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error! Division by zero is impossible")
        return None
x = 10
y = 0
result2 = divide_numbers(x, y)

if result2 is not None:
    print(f'{result2}')



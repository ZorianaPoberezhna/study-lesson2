def called_decorator(function):
    def wrapper(*args, **kwargs):
        print('Function is been called')
        result = function(*args, **kwargs)
        print('Function is been called')
        return result
    return wrapper


@called_decorator
def some_func(a, b, c):
    print(f'Inside function with a={a}, b={b}, c={c}')
    return a + b + c

print(some_func(1, 2, 3))
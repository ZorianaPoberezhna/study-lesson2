def function_info(func):

    def wrapper(*args, **kwargs):
        print(f'{func.__name__} is been called with parameters: {args},{kwargs}')
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} return this value: {result}')
        return result

    return wrapper

@function_info
def some_func(a, b, c):
    return a + b + c

some_func(1, 2, 3)
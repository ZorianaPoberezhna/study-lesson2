def type_checker(*target_types):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for arg in args:
                if not isinstance(arg, target_types):
                    raise TypeError(f"Argument {arg} of type {type(arg)} is not in allowed types {target_types}")

            for kwarg in kwargs.values():
                if not isinstance(kwarg, target_types):
                    raise TypeError(f"Keyword argument {kwarg} "
                                    f"of type {type(kwarg)} is not in allowed types {target_types}")

            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_checker(int, str)
def some_func(a, b, c):
    return f"Arguments: {a}, {b},{c}"
try:
    result = some_func( 1, 'hello', True)
except TypeError as e:
    print(f"Error: {e}")

try:
    result2 = some_func(2, "hello", 10)
    print(result2)
except TypeError as e:
    print(f"Error: {e}")


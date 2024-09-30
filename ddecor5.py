import time


def sleeper(time_to_sleep):

    def decorator(func):

        def wrapper(*args, **kwargs):
            time.sleep(time_to_sleep)
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@sleeper(5)

def some_func(a, b):
    return a + b

result2 = some_func(10, 20)
print(f'Result: {result2}')
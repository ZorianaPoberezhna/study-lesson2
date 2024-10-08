def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)



result = recursive_fibonacci(10)

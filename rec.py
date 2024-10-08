def recursive_sum(n):
        if n < 10:
            return n
        else:
            return n % 10 + recursive_sum(n // 10)

result = recursive_sum(1234)

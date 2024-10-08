import time

def recursive_count_down(n):
    if n <= 0:
        return 1
    else:
        print(n)
        time.sleep(1)
        recursive_count_down(n - 1)

recursive_count_down(10)
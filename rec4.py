def recursive_reverse(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + recursive_reverse(s[:-1])

result = recursive_reverse('hello')

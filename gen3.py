import itertools


def permutations(elements):
    for perm in itertools.permutations(elements):
        yield list(perm)


for i in permutations([1, 2, 3]):
    print(i)



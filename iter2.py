class CyclicIterator:

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iterable:
            raise StopIteration
        value = self.iterable[self.index]
        self.index = (self.index + 1) % len(self.iterable)
        return value

for i in CyclicIterator([1, 2, 3]):
    print(i)

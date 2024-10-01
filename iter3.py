class CyclicIterator:

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
        self.peeked_value = None

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iterable:
            raise StopIteration
        value = self.iterable[self.index]
        self.index = (self.index + 1) % len(self.iterable)
        return value

    def peek(self):
        if not self.iterable:
            raise StopIteration
        if self.peeked_value is None:
            self.peeked_value = self.iterable[self.index]
            return self.peeked_value


cycle_iter = CyclicIterator([1, 2, 3])
print(next(cycle_iter))
print(cycle_iter.peek())
print(next(cycle_iter))
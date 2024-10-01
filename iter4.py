class FilterIterator:

    def __init__(self, iterable, func):
        self.iterable = iterable
        self.func = func
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.iterable):
            value = self.iterable[self.index]
            self.index += 1
            if self.func(value):
                return value
        raise StopIteration


f_iter = FilterIterator([1, 2, 3, 4], lambda x: x % 2 == 0)

while True:
    try:
        next(f_iter)
    except StopIteration:
        break
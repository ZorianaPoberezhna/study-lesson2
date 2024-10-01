class RangeIterator:

    def __init__(self, start, end, step = 1):
        self.current = start
        self.step = step
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            value = self.current
            self.current += self.step
            return value


range_iterator = RangeIterator(1, 10, 2)

for i in range_iterator:
    print(i)
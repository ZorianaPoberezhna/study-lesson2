class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
        self.method_called = 0


    def get_count(self):
        self.method_called += 1
        return Counter.count


c1 = Counter()
c2 = Counter()
result = c1.get_count()

print(c1.method_called)

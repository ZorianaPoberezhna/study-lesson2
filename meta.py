class MetaClass(type):
    def __new__(cls, name, bases, attrs):
        return super().__new__(cls, name, bases, attrs)

    def __init__(self, name, bases, attrs):
        print("Any message")
        super().__init__(name, bases, attrs)

class MyClass(metaclass=MetaClass):
    pass



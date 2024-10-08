class PrivateAttrMeta(type):
    def __new__(cls, name, bases, attrs):

        new_attrs = {}
        for attr_name, attr_value in attrs.items():
            if attr_name.startswith('__') and not attr_name.endswith('__'):
                new_attrs[f'__private_{attr_name[2:]}'] = attr_value
            else:
                new_attrs[attr_name] = attr_value
        return super().__new__(cls, name, bases, new_attrs)

class MyClass(metaclass=PrivateAttrMeta):
    def __init__(self):
        self.__private_var = "It is a private attribute"
        self.public_var = "It is a public attribute"

instance = MyClass


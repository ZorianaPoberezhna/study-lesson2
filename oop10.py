class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, wheels=4):
        super().__init__(make, model)
        self.wheels = wheels

    def get_info(self):
        return f"{super().get_info()}, Wheels: {self.wheels}"

class Moto(Vehicle):
    def __init__(self, make, model, wheels=2):
        super().__init__(make, model)
        self.wheels = wheels

    def get_info(self):
        return f"{super().get_info()}, Wheels: {self.wheels}"

car = Car("Toyota", "Camry")
moto = Moto("Harley-Davidson", "Sportster")

car.get_info()
moto.get_info()
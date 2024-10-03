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

class Electric:
    def __init__(self):
        self.__battery = 0

    def charge(self):
        self.__battery = 100
        print("Battery charged to 100%")

    def get_battery_status(self):
        return f"{self.__battery}"

class ElectricCar(Car, Electric):
    def __init__(self, make, model, wheels=4):
        Car.__init__(self, make, model, wheels)
        Electric.__init__(self)

    def get_info(self):
        return f"{super().get_info()}, {self.get_battery_status()}"

class ElectricMoto(Moto, Electric):
    def __init__(self, make, model, wheels=2):
        Moto.__init__(self, make, model, wheels)
        Electric.__init__(self)

    def get_info(self):
        return f"{super().get_info()}, {self.get_battery_status()}"


car = Car("Toyota", "Camry")
moto = Moto("Harley-Davidson", "Sportster")
electric_car = ElectricCar("Tesla", "Model S")
electric_moto = ElectricMoto("Zero", "SR/F")


print(Car.mro())
print(Moto.mro())
print(ElectricCar.mro())
print(ElectricMoto.mro())
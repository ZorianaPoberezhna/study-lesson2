class Vehicle:
    def __init__(self, name, speed, cost):
        self.name = name
        self.speed = speed
        self.cost = cost


    def __gt__(self, other):
        return self.speed > other.speed


    def __str__(self):
        return (f"{self.name}"
                f"Speed: {self.speed} km/h,"
                f"Cost: {self.cost}$")


v1 = Vehicle("Name1", 100, 10000)
v2 = Vehicle("Name2", 110, 9000)

result = sorted([v1, v2])
print("Sorted by speed:")

for vehicle in result:
    print(vehicle)

print(f"v1 > v2: {v1 > v2}")

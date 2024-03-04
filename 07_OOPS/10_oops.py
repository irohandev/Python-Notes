# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

class Battery:
    def battery_info(self):
        return "This is battery"


class Engine:
    def engine_info(self):
        return "This is Engine"


class ElectricCar(Battery, Engine, Car):
    pass

my_tesla = ElectricCar("Tesla", "Model X")
print(my_tesla.battery_info())
print(my_tesla.engine_info())

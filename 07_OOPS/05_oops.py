# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
        
    def fuel_type(self):
        return "Petrol or Deisel"

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"
        
my_tesla = ElectricCar("Tesla" , "Model Y" , "85 kWH")
print(my_tesla.model)
print(my_tesla.brand)
print(my_tesla.fuel_type())

my_car = Car("Toyota" , "Fortuner")
print(my_car.brand)
print(my_car.model)
print(my_car.fuel_type())
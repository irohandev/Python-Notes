# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.


class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
my_tesla = ElectricCar("Tesla" , "Model Y" , "85 kWH")
print(my_tesla.model)
print(my_tesla.brand)
print(my_tesla.full_name())

# Point:
# 1. inherit krwane ke liye just naya class banao aur uske brace mein super class ka name lik do.
# 2. aur super init function isliye use kiye hai kyuki woh super class ke attribute ka access khudh se apne ap le le.
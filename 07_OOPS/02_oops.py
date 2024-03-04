# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).


class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota" , "Fortune")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

# Point:
# 1. idhr ek class mein hi naya function banaye hai aur usko full name ouput dene ke liye f string use kiye hue hai.
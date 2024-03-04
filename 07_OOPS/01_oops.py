# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.


class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota" , "Fortuner")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata" , "Harrier")
print(my_new_car.brand)
print(my_new_car.model)


# Point:
# 1. init function jo hai usko hamesa likhna hai kyuki woh construction hai..python mein aisa constructor hota hai
# 2. aur class keyword ka use karte hai class banane ke liye.
# 3. Self keyword ek connection ke liye use kiya jta hai attributes ke andar mein.


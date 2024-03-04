# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.
class Car:
    total_car = 0
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
        Car.total_car +=1


my_car = Car("Toyota" , "Fortuner")
my_car2 = Car("Honda" , "Civic")
my_new_car = Car("Tata" , "Harrier")
print(my_car.brand)
print(my_car.model)
print(my_new_car.brand)
print(my_new_car.model)
print(Car.total_car)

# Point:
# 1. Total_car se pata chal raha hai ki kitne baar object create ho rha hai !
# 2. Total_car ko call kanre ke liye bass class name ke sath . {Dot} lgakar call karte hai 
# 3. Print karwane ke liye hm usko variable bana rahe hai warna direct call kar sakte hai
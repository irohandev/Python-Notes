# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.


class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
        
        
    @staticmethod
    def car_desc():
        return "Car is a means of transport"

Car("Toyota" , "Fortuner")
print(Car.car_desc())

# POINTS:
# 1. Static woh funtion hai jisko sirf class se access karte na ki object se aur insab static funtions ko hm python mein decorators kehte hai.
# 2. Statinc func banane ke liye @staticmethod keyword ka use karte hai just woh funtion se phle aur agar self keyword ya  object ke sath call karnge toh error ayega.
# 3. Self keyword ka jrurt nahi hota hai ispe communication line banane ke liye.

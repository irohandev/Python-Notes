# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand , model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand + "!"


my_car = Car("Toyota" , "Fortuner")
#print(my_car.__brand)
print(my_car.get_brand())


#Points:
#1. Python mein kisi bhi attribute ko private krne ke liye uske samne bs 2 underscore lgana padta hai.
#2. print statement isliye comment kiya hua hai kyuki hmlog brand ko get_brand function se access karr sakte hai na ki direct usko access kar sakte hai!
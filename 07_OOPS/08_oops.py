# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.__model = model
    
    
    @property
    def model(self):
        return self.__model
    
my_car = Car("Tata","Safari")
#my_car.model="Nexon"

print(my_car.model)


# POINTS:
# 1. @property keyword se bhi ek decorator banaye aur model func bnaye jisse woh model ko koi bhi over ride nhi kr sake ho hm commentout kiye hai 
# 2. aur jidhr bhi model use kr rhe the class ke andar wala na ki input wale ko hamloh private bana denge __ [2 underscore] use krke 
# 3. toh agr phr over ride krnge toh ab woh error dega isliye ham usko chnge nhi kr skte hai.
# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle(rad):
    area = math.pi * rad **2
    circumference = 2 * math.pi * rad
    return area , circumference

rad = float(input("Enter the radius : "))
a , c = circle(rad)
print("Circumference of the circle :",c)
print("Area of the circle :", a)


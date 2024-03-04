# 1. Basic Function Syntax
# Problem: Write a function to calculate and return the square of a number.

def square(number):
    return number**2
    

number = int(input("Enter the number to calculate the square : "))
result = square(number)

print("Your calculated square of the input is :",result)

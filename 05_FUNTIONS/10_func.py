# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

def factorial(number):
    if number == 0:
        return 1
    else:
        return number*factorial(number-1)

number = int(input("Enter the number : "))
print(factorial(number))
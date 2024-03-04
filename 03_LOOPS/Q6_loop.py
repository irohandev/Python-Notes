# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

number = int(input("Enter the number whose factorial is to be calculated : "))
factorial = 1

while number>0:
    factorial = factorial*number
    number -=1

print("Factorial of the given input is - ", factorial)
# 2. Function with Multiple Parameters
# Problem: Create a function that takes two numbers as parameters and returns their sum.

def sum(first , second):
    return first+second

first = int(input("Enter first number : "))
second = int(input("Enter second number : "))
result = sum(first , second)

print("Result of the input is :", result)
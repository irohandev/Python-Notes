# 8. Prime Number Checker
# Problem: Check if a number is prime.

number = int(input("Enter the number : "))
prime = True

if number >1:
    for i in range(2, number+1):
        if (number % i) == 0:
            prime = False 
            break
        
print(prime)
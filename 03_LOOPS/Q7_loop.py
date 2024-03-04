# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    n = int(input("Enter input : "))
    
    if 1 <= n <= 10:
        print("You are out of the loop !")
        break
    else:
        print("Invalid choice, try again!")
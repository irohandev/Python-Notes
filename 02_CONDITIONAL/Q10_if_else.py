# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. 
# (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

Animal = input("Enter your Pet details : ")
Age = int(input("Enter your pet's age : "))

if Animal == "Dog":
    if Age <= 2:
        print("Puppy food recommended")
    elif Age > 2 and Age <=5:
        print("Adult dog food recommended")
        
elif Animal == "Cat":
    if Age <= 2:
        print("Kitty food recommended")
    elif Age > 2 and Age <=5:
        print("Adult cat food recommended")

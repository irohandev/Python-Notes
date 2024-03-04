# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children.
# Everyone gets a $2 discount on Wednesday.

day = input("Enter the day : ")
age = int(input("Enter your age : "))

if day == 'Wednesday':
    if age < 18:
        price = 8
        print("Price of ticket = ", +price-2)
    else:
        price = 12
        print("Price of ticket =", +price-2)
    
else:
    if age > 18:
        price = 12
        print("Price of ticket = ", +price)
    else:
        price = 8
        print("Price of ticket = ", +price) 

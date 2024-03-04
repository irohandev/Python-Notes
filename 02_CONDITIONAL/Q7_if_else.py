# 7. Coffee Customization
# Problem: Customize a coffee order:
# "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.


order_size = input("Enter the coffee size : ")
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order: ", coffee)
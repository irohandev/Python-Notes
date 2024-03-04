# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

input_str = input("Enter your string : ")


for char in input_str:
    print(char)
    if input_str.count(char)==1:
        print("Your first non-repeated character is : ", char)
        break
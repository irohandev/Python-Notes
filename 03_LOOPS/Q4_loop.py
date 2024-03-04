# 4. Reverse a String
# Problem: Reverse a string using a loop.

input_str = input("Enter the String which is to be reversed : ")
reversed_str = ""
for i in input_str:
    reversed_str = i + reversed_str

print("Your reversed string is : ", reversed_str)
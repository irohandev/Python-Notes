# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]

mylist=[]
number = int(input("Enter the number of item which is to be present in the list : "))

unique_list = set()

for i in range(number):
    element=input("Enter list  elements : ")
    
    mylist.append(element)

print(mylist)
    
for item in mylist:
    if item in unique_list:
        print("Duplicate item :", item)
        break
    unique_list.add(item)
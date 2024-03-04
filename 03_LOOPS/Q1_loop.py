# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

n = int(input("Enter the list count : "))
mylist= []
pos = 0

for i in range(n+1):
    ele = int(input("Enter the list element: "))
    mylist.append(ele)
    
    if ele>0:
        pos+=1

print("Your original list : ", mylist)
print("Final count of your Positive Number is list is: ", pos)
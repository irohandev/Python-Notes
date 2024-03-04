# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = int(input("Enter the age = "))

if age < 13:
    print("Child")
elif 13<age<=19:
    print("Teenager")
elif 20<=age<=59:
    print("Adult")
else:
    print("Senior")
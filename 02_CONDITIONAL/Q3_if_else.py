# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score:
# A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

marks = int(input("Enter the marks obtained : "))

if marks <100  and marks >= 90:
    print("A Grade")

elif marks <90  and marks >= 80:
    print("B Grade")

elif marks <80  and marks >= 70:
    print("C Grade")

elif marks <70  and marks >= 60:
    print("D Grade")
    
elif marks <  60:
    print("E Grade")
    

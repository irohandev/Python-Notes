# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather 
# (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

Weather = input("Enter the weather type : ")

if Weather == "Sunny":
    print("Go for walk")

elif Weather == "Rainy":
    print("Read a book")
    
elif Weather == "Snowy":
    print("Build a snowman")
    
else:
    print("Please provide proper details!")
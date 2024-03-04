# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
        
print_kwargs(Name = "Rohan", Course = "B.Tech")
print_kwargs(Name = "Rohan")
print_kwargs(Name = "Rohan", Course = "B.Tech", Dept = "CSE")


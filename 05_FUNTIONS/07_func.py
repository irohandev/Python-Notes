# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def add(*args):
    print(args)
    return sum(args)

print(add(1,2,3,4))


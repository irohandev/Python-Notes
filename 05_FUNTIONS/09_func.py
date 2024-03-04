# 9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i
    
n = int(input("Enter the limit: "))
for i in even_generator(n):
    print(i)
    
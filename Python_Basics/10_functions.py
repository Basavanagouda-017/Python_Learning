# 1. Simple Function
def greet():
    print("Hello Bro!")

greet()


# 2. Function with Parameters
def greet_user(name):
    print("Hello", name)

greet_user("Darshan")
greet_user("Rahul")


# 3. Function Returning a Value
def add(a, b):
    return a + b

result = add(10, 20)
print(result)


# 4. Difference between print and return
def square_print(n):
    print(n * n)

def square_return(n):
    return n * n

square_print(5)
print(square_return(5))
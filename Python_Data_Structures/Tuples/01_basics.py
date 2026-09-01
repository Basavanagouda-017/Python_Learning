#Tuples are same like lists only the diff is they are immutable 
# Creating Tuples
numbers = (10, 20, 30)
print(numbers)

# Mixed Data Types
data = (10, "Python", 3.14, True)
print(data)

# Single Element Tuple
t = (10,)
print(type(t))

# Indexing
print(numbers[0])
print(numbers[-1])

# Slicing
print(numbers[1:])
print(numbers[::-1])

# Packing
student = "Darshan", 20, "Python"
print(student)

# Unpacking
name, age, course = student

print(name)
print(age)
print(course)

# Swapping
a = 10
b = 20

a, b = b, a

print(a, b)
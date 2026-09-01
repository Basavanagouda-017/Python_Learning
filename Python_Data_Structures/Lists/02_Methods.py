# List Methods

numbers = [10, 20, 30, 40]
numbers.append(50)
print(numbers)

numbers.extend([60, 70])
print(numbers)

numbers.insert(2, 25)
print(numbers)

numbers.remove(25)
print(numbers)

numbers.pop()
print(numbers)

# Useful Functions
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Copy
a = [1, 2, 3]
b = a
c = a.copy()
b.append(4)
print(a)
print(b)
print(c)
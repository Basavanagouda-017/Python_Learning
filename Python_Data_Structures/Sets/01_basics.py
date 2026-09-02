# Creating a Set
numbers = {10, 20, 30, 40}
print(numbers)

# Duplicate values are removed automatically
numbers = {10, 20, 20, 30, 30, 40}
print(numbers)

# Empty Set
empty_set = set()
print(type(empty_set))

# Membership Test
print(20 in numbers)
print(100 in numbers)

# Looping through a Set
for num in numbers:
    print(num)

# Converting List to Set
values = [10, 20, 20, 30, 40, 40, 50]
unique_values = set(values)
print(unique_values)
print(len(unique_values))
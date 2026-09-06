#Raise Is an error showcasing the use of raise in python

# raise ValueError("This is a custom error message")


age = int(input("Enter age: "))

if age < 18:
    raise ValueError("Age must be at least 18.")

print("Eligible")
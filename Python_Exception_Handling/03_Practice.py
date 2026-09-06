# 💻 Mini Coding Challenge

# Write a program that:

# Takes a number as input.
# Uses try and except ValueError.
# If the input is valid, print:
# Square = <number * number>
# Use the else block to print:
# Calculation completed successfully.

# Example:

# Input:

# 8

# Output:

# Square = 64
# Calculation completed successfully.



try:
    num=int(input("Enter a number: "))

except ValueError:
    print("Invalid Input")

else:
    print("Square =", num * num)
    print("Calculation completed successfully.")    

# 💻 Final Challenge

# Write a program that:

# Takes the user's age as input.
# If age is less than 18, use raise to generate:
# ValueError("You must be 18 or older.")
# Otherwise print:
# Access Granted



try:
    age=int(input("Enter Age :"))
    
except ValueError:
    print("Invalid Input")
    
else:
    if age<18:
        raise ValueError("You Must Be 18 or older")
    else:
        print("Access Granted")
#         try
#          │
#    ┌─────┴─────┐
#    │           │
# No Error     Error
#    │           │
#    ▼           ▼
# #  else       except


try:
    age=int(input("Enter Age:"))
    print("You are eligible to vote")

except ValueError:
    print("Invalid Input")

else:
    if age<18:
        print("You are not eligible to vote")
    else:
        print("You are eligible to vote")
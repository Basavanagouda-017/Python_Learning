try:
    nums=int(input("Enter a number: "))
    print(10/nums)

except ZeroDivisionError:
    print("You cannot divide by zero.")

except ValueError:
    print("Invalid  Input")
    
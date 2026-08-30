#if 

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")




#if else

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")



#if-elis-else

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")




#Nested if-else
age = int(input("Enter your age: "))
license = input("Do you have a driving license? (yes/no): ")

if age >= 18:
    if license.lower() == "yes":
        print("You can drive.")
    else:
        print("You need a driving license.")
else:
    print("You are underage.")
# In this Code we can see tht how the class variable is used in python and  also  how to create instance variable in python.
# Create an Employee class:

# Class Variable
# company = "Google"
# Instance Variables
# name
# salary
# Method
# display()

# Expected output:

# Company : Google
# Employee : Darshan
# Salary : 50000

# Company : Google
# Employee : Rahul
# Salary : 60000


class Employee:
    company="Google"
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def display(self):
        print("Company :",self.company)
        print("Employee : ",self.name)
        print("Salary :",self.salary)
        
        
e1=Employee("Darshan",50000)
e2=Employee("Rahul",60000)

e1.display()
e2.display()

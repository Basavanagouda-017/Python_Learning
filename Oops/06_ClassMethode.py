# This is a Python code that demonstrates the use of class methods and class variables in a class called `Student`.
# 💻 Coding Challenge
# Create a Student class.

# Class Variable
# college = "MIT"
# Constructor
# name
# Class Method
# change_college(new_college)


class Student:
    college="MIT"
    
    def __init__(self,name):
        self.name=name
        
    @classmethod
    def change_college(cls,new_college):
        cls.college=new_college
s1=Student("Darshan")
s2=Student("Rahul")
print(s1.college)
print(s2.college)

Student.change_college("KLE")


print(s1.college)
print(s2.college)
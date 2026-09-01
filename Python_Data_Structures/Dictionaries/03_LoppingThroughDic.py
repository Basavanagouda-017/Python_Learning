student = {
    "Math": 95,
    "Science": 90,
    "English": 88
}

# Print all subjects.
# Print all marks.
# Print subject and mark together in this format:


#method1
for key in student.keys():
    print(key)


#method2    
for value in student.values():
    print(value)

#method3    
for key,value in student.items():
    print(key," : ",value)
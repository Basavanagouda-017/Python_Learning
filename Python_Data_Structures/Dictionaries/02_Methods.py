#get()
student={
    "name": "Darshan",
    "age":21,
    "roolno":15
}
print(student.get("name"))
print(student.get("age"))
print(student.get("roolno","Not Fount"))


#keys()
print(student.keys())


#values
print(student.values())


#items Return both keys and values
print(student.items())


#pop()
print(student.pop("roolno"))
print(student)



#update()
student.update(
    {
        "name": "Rahul",
        "course": "Python"
    })
    
    
print(student)
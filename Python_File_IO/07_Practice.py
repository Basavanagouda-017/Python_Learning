# 💻 Mini Challenge

# Suppose students.txt contains:

# Darshan
# Rahul
# Aman
# Kiran

# Write a program that:

# Opens the file.
# Uses readlines().
# Prints each student's name using a for loop.
# Remove the extra newline using strip().
# Closes the file.


#write
f=open("students.txt","w")
f.write("Darshan\nRahul\nAman\nKiran")
f.close()


#read
f=open("students.txt","r")
lines=f.readlines()
for line in lines:
    print(line.strip())
f.close()


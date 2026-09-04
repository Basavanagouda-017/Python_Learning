# Create a program using with open() that:

# Creates a file named goals.txt.
# Writes these goals:
# Get Internship
# Master Python
# Build Projects
# Opens the same file again using with open() in read mode.
# Prints the contents.


with open("goals.txt", "w") as f:
    f.write("Get Internship\n")
    f.write("Master Python\n")
    f.write("Build Projects\n")

with open("goals.txt", "r") as f:
    contents = f.readlines()

    for c in contents:
        print(c.strip())
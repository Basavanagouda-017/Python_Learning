# Split & Join

languages = "Python,Java,C++"
lst = languages.split(",")
print(lst)
print(" | ".join(lst))

# Checking Methods

print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("   ".isspace())

# Mini Practice
name = "Machine Learning"
print(name[0])
print(name[-1])
print(name[::-1])
print(len(name))
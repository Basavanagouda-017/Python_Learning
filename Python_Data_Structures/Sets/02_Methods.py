

colors = {"Red", "Blue", "Green"}

# add()
colors.add("Yellow")
print(colors)

# update()
colors.update(["Black", "White"])
print(colors)

# remove()
colors.remove("Blue")
print(colors)

# discard()
colors.discard("Pink")   # No Error
print(colors)

# pop()
removed = colors.pop()
print("Removed:", removed)
print(colors)

# clear()
colors.clear()
print(colors)
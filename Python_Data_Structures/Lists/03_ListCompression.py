squares = [x * x for x in range(1, 6)]
print(squares)

even = [x for x in range(1, 11) if x % 2 == 0]
print(even)

# ------------------------------
# Mini Practice
# ------------------------------

marks = [45, 67, 89, 90, 56]

print(max(marks))
print(min(marks))
print(sum(marks))

passed = [mark for mark in marks if mark >= 50]
print(passed)
A = {1, 2, 3}
B = {3, 4, 5}

# Union
print("Union:", A | B)
print("Union:", A.union(B))

# Intersection
print("Intersection:", A & B)
print("Intersection:", A.intersection(B))

# Difference
print("Difference (A-B):", A - B)
print("Difference (B-A):", B - A)

# Symmetric Difference
print("Symmetric Difference:", A ^ B)
print("Symmetric Difference:", A.symmetric_difference(B))
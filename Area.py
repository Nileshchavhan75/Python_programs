A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))         # Union → {1, 2, 3, 4, 5, 6}
print(A.intersection(B))  # Intersection → {3, 4}
print(A.difference(B))    # Difference → {1, 2}
print(A.symmetric_difference(B))  # Symmetric Difference → {1, 2, 5, 6}

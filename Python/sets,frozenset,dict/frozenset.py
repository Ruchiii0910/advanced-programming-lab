# Frozen Set

fs = frozenset([10, 20, 30, 40])

print("Frozen Set:", fs)

fs2 = frozenset([30, 40, 50])

print("Union:", fs.union(fs2))

print("Intersection:", fs.intersection(fs2))

print("Difference:", fs.difference(fs2))

print("Symmetric Difference:", fs.symmetric_difference(fs2))

print("Is 20 present:", 20 in fs)

print("Length:", len(fs))

print("Is subset:", fs.issubset(fs2))

print("Is superset:", fs.issuperset(fs2))

print("Is disjoint:", fs.isdisjoint(fs2))
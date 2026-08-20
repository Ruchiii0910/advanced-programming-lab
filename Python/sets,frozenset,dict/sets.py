# Set

s = {10, 20, 30, 40}

print("Set:", s)

s.add(50)
print("After add:", s)

s.update([60, 70])
print("After update:", s)

s.remove(20)
print("After remove:", s)

s.discard(100)
print("After discard:", s)

print("Copy:", s.copy())

s2 = {30, 40, 80}
print("Union:", s.union(s2))

print("Intersection:", s.intersection(s2))

print("Difference:", s.difference(s2))

print("Is 30 present:", 30 in s)
student = {
    "name": "Ruchita",
    "age": 20,
    "course": "Computer Science"
}

print("Dictionary:", student)

print("Keys:", student.keys())

print("Values:", student.values())

print("Items:", student.items())

print("Name:", student.get("name"))

student.update({"age": 21})
print("After update:", student)

student["college"] = "DYP CET"
print("After adding:", student)

student.pop("age")
print("After pop:", student)

print("Copy:", student.copy())

print("Length:", len(student))
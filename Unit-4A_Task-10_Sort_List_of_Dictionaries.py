students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Priya", "marks": 95},
    {"name": "Arjun", "marks": 75},
    {"name": "Sneha", "marks": 90}
]

ascending = sorted(students, key=lambda x: x["marks"])
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("Ascending Order:")
for student in ascending:
    print(student)

print("Descending Order:")
for student in descending:
    print(student)

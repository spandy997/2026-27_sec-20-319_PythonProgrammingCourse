students = {
    1: {"name": "Rahul", "marks": 85},
    2: {"name": "Priya", "marks": 90},
    3: {"name": "Arjun", "marks": 78}
}

for student in students.values():
    print("Name:", student["name"])
    print("Marks:", student["marks"])

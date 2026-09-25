# ===============================
# practice - 01 Nested Dictionary
# ===============================
students = {
    "student1": {
        "name": "Atul Paul",
        "age": 22,
        "marks": 85
    },
    "student2": {
       "name": "Ankit Paul",
       "age": 9,
       "marks": 99
    },
    "student3": {
        "name": "Karim",
        "age": 21,
        "marks": 92
    }
}

# 1. Atul's name
print(students["student1"]["name"])
# 2. Ankit's age
print(students["student2"]["age"])
# 3. Karim's marks
print(students["student3"]["marks"])
# 4. Print every student's name and marks
for student_id, student in students.items():
    print(
        "name:", student["name"],
        "| marks:", student["marks"]
    )


# ===============================
# practice - 02 Nested Dictionary
# ===============================
student = {
    "name": "Atul",
    "skills": ["Python", "SQL", "Java"]
}
# 1. Add Machine Learning
student["skills"].append("Machine Learning")
print(student)
# 2. Remove Java
student["skills"].remove("Python")
print(student)
# 3. Print all skills
for skill in student["skills"]:
    print(skill)

# ==================================
# practice - 03 List of Dictionaries
# ==================================
students1 = [
    {"name": "Atul Paul", "marks": 84},
    {"name": "Ankit Paul", "marks": 98},
    {"name": "Rahim", "marks": 78},
    {"name": "Karim", "marks": 92},
    {"name": "Sakib", "marks": 88}
]

for student in students1:
    if student["marks"] > 80:
        print(student["name"])

# ======================================
# practice - 04 Dictionary Comprehensive
# ======================================
numbers = range(1, 11)

squares = {
    number: number * number
    for number in numbers
}
print(squares)


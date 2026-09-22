# ==========================================
# Practice - Dictionaries
# ==========================================

print("--- Practice 1 ---")
student_p1 = {
    "name": "Atul",
    "age": 21,
    "department": "CIS",
    "university": "DIU"
}
print(student_p1["name"])


print("\n--- Practice 2 ---")
student_p2 = {
    "name": "Atul",
    "age": 22,
    "department": "CIS"
}
student_p2["age"] = 23
student_p2["city"] = "Manikganj"
print(student_p2["department"])
del student_p2["name"]


print("\n--- Practice 3 ---")
student_p3 = {
    "name": "Atul",
    "age": 22,
    "department": "SWE",
    "skills": ["Python", "SQL", "Java"]
}
print(student_p3["name"])
print(student_p3["age"])
print(student_p3["department"])
for skill in student_p3["skills"]:
    print(skill)


print("\n--- Practice 4 (Loop) ---")
student_p4 = {
    "name": "Atul",
    "age": 22,
    "department": "CIS"
}
for key, value in student_p4.items():
    print(f"{key} : {value}")


print("\n--- Practice 5 (Nested) ---")
students_p5 = {
    "student1": {
        "name": "Atul",
        "marks": 85
    },
    "student2": {
        "name": "Rahim",
        "marks": 78
    },
    "student3": {
        "name": "Karim",
        "marks": 92
    }
}

print(students_p5["student1"]["marks"])

print(students_p5["student2"]["name"])

print(students_p5["student3"]["marks"])

print("\n--- All students ---")
for student_id, details in students_p5.items():
    print(f"{details['name']} - {details['marks']}")
students = {
    "student1": {
        "name": "Atul Paul",
        "age": 21,
        "marks": 85
    },
    "student2": {
        "name": "Ankit paul",
        "age": 9,
        "marks": 78
    }
}

# data access
print(students["student1"]["name"])
print(students["student1"]["marks"])

print(students["student2"]["age"])

# nested dictionary update
students["student1"]["marks"] = 95
print(students["student1"]["marks"])

# Nested Dictionary Loop 
print("========= Dic Loop =========")
for student_id, data in students.items():
    print(student_id)
    print(data)

for student_id, data in students.items():
    print("ID:", student_id)
    print("Name:", data["name"])
    print("Marks:", data["marks"])

student = {
    "name": "Atul",
    "skills": [
        "Python",
        "SQL",
        "Java"
    ]
}

print(student["skills"])
print(student["skills"][0])
student["skills"].append("Machine Learning")
print(student["skills"][3])
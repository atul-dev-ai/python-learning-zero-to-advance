student = {
    "name": "Atul",
    "age": 21,
    "department": "CIS",
    "university": "DIU"
}

for key in student:
    print(key)

for key in student:
    print(student[key]) # values

print("========== Key + Value by items() =============")
for key, value in student.items():
    print(key + ":", value)

# Nested Dictionaries
students = {
    "student1": {
        "name": "Atul Paul",
        "age": 21
    },
    "student2": {
        "name": "Ankit Paul",
        "age": 9
    }
}

print(students["student1"]["name"])
print(students["student2"]["age"])

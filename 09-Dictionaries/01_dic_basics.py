"""
A Dictionary stores data in KEY : VALUE pairs
{} -> Dictionary
:  -> Key ebong value alada kore
,  -> Ekadhik item alada kore
"""

student = {
    "name": "Atul",
    "age": 21,
    "department": "CIS",
    "university": "DIU"
}

print(student["name"])
print(student["age"])
print(student["department"])
print(student["university"])

student["age"] = 22
print(student)

# New item add
student["city"] = "Manikganj"
print(student)
del student["age"]
print(student)

# pop()
student["age"] = 21
print(student)


age = student.pop("age")
print(age)
print(student)

#get()
# print(student["email"]) KeyError
print(student.get("email")) # Output: None
print(student.get("email", "Not Found"))

# Show all Keys
print(student.keys())

# show all values
print(student.values())

# Show all items. both key and values
print(student.items())

# Length
print(len(student))

print("name" in student)
print("age" in student)
print("email" in student)

# update()
# eksathe notun data add ba existing data update kora jay.
student.update({
    "department": "Computing & Information System",
    "university": "Daffodil International University"
})
print(student)

# clear()
# student.clear()
# print(student) #Empty
# {} this is a empty dictionary but not a empty set()

for key in student:
    print(key)

for key in student:
    print(student[key]) # values

print("========== Key + Value by items() =============")
for key, value in student.items():
    print(key+":", value)

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


# List under Dictionary
student1 = {
    "id": 101,
    "name": "Atul Paul",
    "age": 21,
    "department": "Computing & Information System",
    "university": "Daffodil International University",
    "skills": ["Python", "Java", "SQL", "React"]
}

print(student1["skills"])
print(student1["skills"][0])
student1["city"] = "manikganj"
print(student1)
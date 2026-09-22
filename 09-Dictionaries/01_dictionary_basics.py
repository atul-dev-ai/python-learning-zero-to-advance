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

# Modify value
student["age"] = 22
print(student)

# New item add
student["city"] = "Manikganj"
print(student)

# Delete item
del student["age"]
print(student)

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

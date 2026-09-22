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
student.pop("age")
print(student)
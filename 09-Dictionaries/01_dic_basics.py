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
student.clear()
print(student) #Empty
# {} this is a empty dictionary but not a empty set()


student = {
    "name": "Atul",
    "age": 21,
    "department": "CIS",
    "university": "DIU"
}

# pop()
age = student.pop("age")
print(age)
print(student)

# get()
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

# Check if key exists
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

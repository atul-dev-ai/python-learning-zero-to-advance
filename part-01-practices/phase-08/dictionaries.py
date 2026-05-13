"""
Dictionary holo key-value pair collection
boishito:
    - key thake
    - value thake
    - fast lookup
    - mutable
"""

# sets er moto {} backet use kora hoy
student = {
    "name": "Atul",
    "age": 21,
    "department": "CIS",
}
# access
print(student['name'])

# safer access (jodi .get use kori tahole sekhane [] backet use kora jabe na first backet() use korte hobe.)
print(student.get('age'))

# add/update
student['cgpa'] = 3.75
student["age"] = 22

student.update({
    "cgpa": 4
})

print(student)

# loop through dictionary
for key in student:
    print(key)
    print(key, ':', student[key])
    # keys, values, items
    print(student.keys())
    print(student.values())
    print(student.items())


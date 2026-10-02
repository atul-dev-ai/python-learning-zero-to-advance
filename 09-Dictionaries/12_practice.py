students = [
    {
        "name": "Atul Paul",
        "marks": {
            "Python": 90,
            "Database": 85,
            "Math": 88
        }
    },

    {
        "name": "Rahim",
        "marks": {
            "Python": 82,
            "Database": 90,
            "Math": 80
        }
    },

    {
        "name": "Karim",
        "marks": {
            "Python": 95,
            "Database": 88,
            "Math": 92
        }
    }
]

for student in students:

    print(student["name"])

    for subject, mark in student["marks"].items():
        print(subject, ":", mark)
    print()

# Total Marks
for student in students:
    total = 0

    for mark in student["marks"].values():
        total += mark

    print(student["name"], "Total:", total)

# Highest Marks
highest_student = ""
highest_total = 0

for student in students:
    total = 0

    for marks in student["marks"].values():

        total += mark

    if total > highest_total:
        highest_total = total
        highest_student = student["name"]

print("Highest Student: ", highest_student)
print("Highest Total: ", highest_total)

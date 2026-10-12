def student_result(name, marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 40:
        status = "Pass"
    else:
        status = "Fail"
    return total, average, status

result = student_result("Atul Paul", [80, 94, 88])
print("Total:", result[0])
print("Average:", result[1])
print("Status:", result[2])

# with *args
def calculate_total(*marks):
    total = 0

    for mark in marks:
        total += mark

    return total

print(calculate_total(80, 75, 90))
print(calculate_total(60, 10, 222))
print(calculate_total(50, 70, 60, 80))

'''
*marks collects any number of positional arguments into a tuple,
alowing the function to accept a flexible number of marks.
'''

# With *kwargs
def student_info(**info):
    for key, value in info.items():
        print(key, ":", value)

student_info (
    name = "Atul Paul",
    department = "CIS",
    university = "DIU",
    semester = 5
)

# filter() + map()
'''
filter() selects passing marks,
map() adds five bonus points, and
list() converts the result into a list.
'''
marks = [35,80, 45, 90, 25, 70]
passed = filter (
    lambda mark: mark >= 40, marks
)

bonus = list (
    map (
        lambda mark: mark + 5, passed
    )
)
print(bonus)


# dictionary theke top student ber kora:
students = {
    "Atul Paul": 85,
    "Ankit": 99,
    "Anik": 92,
    "Sakib": 35,
    "Nabil": 48
}

top_students = sorted (
    filter (
        lambda item: item[1] >= 70, students.items()
    ),
    key= lambda item: item[1], reverse=True
)

print(top_students)
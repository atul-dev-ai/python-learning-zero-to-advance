import numpy as np
'''
Boolean indexing is a technique use to select elements from an array 
based on Boolean conditions (True / False).
'''

marks = np.array([35, 45, 55, 65, 75, 85])

result = marks > 40
print(result)

# boolean indexing
passed_marks = marks[marks > 40]

print(passed_marks)

# AND
result = marks[(marks > 40) & (marks < 80)]
print(result)

# OR 
print(marks[(marks < 40) | (marks > 80)])

# NOT 
print(marks[~(marks > 50)])


# names np array
names = np.array([
    "Atul",
    "Ankit",
    "Sakib",
    "Nabil",
    "Hasan",
    "Rahim",
    "Karim",
    "Anik"
])

marks = np.array([85, 35, 65, 45, 90, 80, 60, 50])

# find passed students
passed = marks >= 40
print("Passed Students: ")
print(names[passed])
print("Passed marks: ")
print(marks[passed])

# np.where() 
result = np.where(marks >= 40, "Pass", "Fail")
print(result)

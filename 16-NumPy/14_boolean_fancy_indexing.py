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

# bonus
bonus_mark = np.where(marks >= 50, marks + 5, marks)
print(bonus_mark)

'''
Fancy Indexing is a NumPy technique that selects specific elements using a list o array of indices. 
It allows you to access multiple elements of an array at once, based on their positions.
'''
# fancy indexing
fancy_index = marks[[1, 3, 5]]
print(fancy_index)


# fancy indexing in 2D array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])

# select row 0 and 2
select_specific_rows = matrix[[0, 2]]
print(select_specific_rows)

# select row 1 and 2
select_rows = matrix[[1, 2]]
print(select_rows)

# row column
rows = [0, 1, 2]
columns = [0, 1, 2]

show_row_column = matrix[rows, columns]
print(show_row_column)

# first select values greater than 50
filtered = marks[marks > 50]
print(filtered)
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
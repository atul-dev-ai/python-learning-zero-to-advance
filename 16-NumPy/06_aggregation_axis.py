
import numpy as np
'''
An aggregation function summaries multiple values into a result, 
such as their sum, mean, minimum or maximum.
'''
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Count:", np.size(marks))
'''
Standard deviation and variance measure how spread out 
the data values are around their mean.
'''
print("Standard Deviation:",np.std(marks))
print("Variance:",np.var(marks))
print("Median:",np.median(marks))

# 2d and axis 
marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [90, 95, 85]
])

student_totals = np.sum(marks, axis = 1)
print(student_totals)
print(np.mean(marks, axis= 1))
print(np.max(marks, axis = 1))
student_totals = np.sum(marks, axis = 0)
print(student_totals)

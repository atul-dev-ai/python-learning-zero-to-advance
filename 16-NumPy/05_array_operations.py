import numpy as np
'''
NumPy supports element-wise arithmetic operations on arrays, 
allowing calculations to be applied to corresponding elements.
'''
numbers = np.array([10, 20, 30, 40, 50])
print(numbers + 5)
print(numbers - 5)
print(numbers * 2)
print(numbers / 2)


# corresponding element arithmetic operations
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# comparison operations
'''
Comparison operations compare array elements and 
return Boolean values: True or False
'''
marks = np.array([35, 50, 65, 80, 95])
print(marks > 60)
print(marks < 50)
print(marks == 80)

'''
Boolean masking selects array elements 
based on a Boolean condition.
'''
result = marks[marks > 60]
print(result)

result = marks[(marks >= 50) & (marks < 90)]
print(result)

result = marks[(marks < 50) | (marks > 80)]
print(result)


# np.where()
marks = np.array([25, 45, 70, 35, 90])
results = np.where(marks >= 40, "Pass", "Fail")
print(results)
# (condition, value_if_true, value_if_false)

'''
An aggregation function summaries multiple values into a result, 
such as their sum, mean, minimum or maximum.
'''
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Count:", np.size(marks))
print(np.std(marks))
print(np.var(marks))
print(np.median(marks))
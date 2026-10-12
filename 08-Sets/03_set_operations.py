# union
"""Union combines all unique elements from two sets"""
python_students = {"Atul", "Rahim", "Karim", "Aditiya"}
java_students = {"Rajat", "Anik", "Sakib", "Rahim"}
all_students = python_students | java_students
print(all_students)
# all_students = python_students.union(java_students)

# Intersection ( & )
# intersection returns elements common to both sets.
common_students = python_students & java_students
print(common_students)
# common_students = python_students.intersection(java_students)

# Difference ( - )
only_python = python_students - java_students
print(only_python)

only_java = java_students - python_students
print(only_java)

# symmetric difference
# operator = ^, symmetric_difference
"""Elements that exist in only one of the sets, but not in both"""
a = {1, 2, 3}
b = {3, 4, 5}
result = a ^ b
print(result) # 3 is excluded because it exists in both sets

# subset
# operator = issubset(), variable <= variable
"""If all elements of a set exist in another set, the first set is a subset"""
c = {1, 2}
d = {1, 2, 3, 4}
print(c.issubset(d))

# superset
"""If a set contains all elements of another set, it is a superset"""
e = {1, 2, 3, 4}
f = {1, 2}
print(e.issuperset(f))

# disjoint set
"""If two sets have no common elements, they are disjoint"""
g = {1, 2, 3}
h = {4, 5, 6}
print(g.isdisjoint(h))

marks = [80, 90, 80, 70, 90, 60]
unique_marks = set(marks)
print(unique_marks) 
"""Converting to a set does not preserve the original list's order or duplicate counts"""

squares = {x ** 2 for x in range(1, 6)}
print(squares)

squaress = {x ** 2 for x in [1, 2, 3, 2]}
print(squaress)

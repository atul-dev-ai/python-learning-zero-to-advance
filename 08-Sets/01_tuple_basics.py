my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set)) # class = SET

student_ids = [101, 102, 103, 104, 105, 101, 102]
unique_ids = set(student_ids)
print(unique_ids)

# data = {[1, 2], [3, 4]}  type error

# integer set
numbers = {1, 2, 3, 4, 5}
print(type(numbers)) # set
print(numbers)

# string set
fruits = {"Apple", "Banana", "Mango"}
print(fruits)

# Mixed data
data = {19, "Python", 3.5, True}
print(data)

# Empty set
empty_set = {}
print(type(empty_set)) # {} ekti empty dictionary create kore

empty_set_01 = set()
print(type(empty_set_01)) # Class = SET

names = ["Atul", "Rahim", "Atul", "Karim", "Rahim"]
print(type(names)) # list
print(names)
unique_names = set(names) # Set
print(unique_names)

for number in numbers:
    print(numbers)

# add()
numbers.add(9) # duplicate value add korle seta unchanged thake.
print(numbers)

# update()
numbers.update([5, 6, 7, 8]) 
print(numbers)

# remove()
numbers.remove(8)
print(numbers)

# discard()
numbers.discard(9) # element thakle badh dey, na thakle error dey
print(numbers)

# pop()
"""set unordered houay kon element
remove hobe ta dhore newa jabe na."""
removed = numbers.pop()
print("Removed: ", removed)
print("Remaining: ", numbers)

# clear()
numbers.clear()
print(numbers) # output = set()

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
"""elements je gula sudu ekti set e ache
    kintu uboy set e common noy"""
a = {1, 2, 3}
b = {3, 4, 5}
result = a ^ b
print(result) # 3 badh jabe karon eti dui set ei ache

# subset
# operator = issubset(), variable <= variable
"""ekti set er sob elements onno set
    er moddhe thakle prothomti subset"""
c = {1, 2}
d = {1, 2, 3, 4}
print(a.issubset(b))

# superset
"""ekti set onno set er \
    sob elements dharon korle seti Superset"""
e = {1, 2, 3, 4}
f = {1, 2}
print(e.issuperset(f))

# disjoint set
"""duita set er moddhe kono common element na thakle
    tara Disjoint"""
g = {1, 2, 3}
h = {4, 5, 6}
print(g.isdisjoint(h))

emails = [
    "atul@gmail.com",
    "Rahim@gmail.com",
    "atul@gmail.com",
    "karim@gmail.com",
    "sakib@gmail.com"
]
print(type(emails)) # list
unique_emails = set(emails)
print(unique_emails)
print(type(unique_emails)) # set


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


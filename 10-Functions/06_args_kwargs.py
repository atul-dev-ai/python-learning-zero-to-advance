# *args
def add(*numbers): # ekhane numbers ekto TUPLE. tai ekhane loop chalano jay.
    total = 0
    
    for number in numbers:
        total += number
    
    return total

print(add(10, 20))
print(add(10, 20, 40))
print(add(10, 20 , 30, 40, 50))

'''
*args onek gula positional argument ney.
kintu jodi onek gula Keyword argument kinte chai
tokhon **kwargs use kora hoy.
*args -> Tuple
**kwargs -> Dictionary
'''
def student_info(**infos):
    print(infos)

student_info(
    name = "Atul Paul",
    age = 21,
    dept = "CIS"
)
# infos ekti dictionary

def add(*numbers):
    total = 0

    for number in numbers:
        total += number
    return total

print(add(10, 5))
print(add(5, 10))
print(add(5, 10, 15))
print(add(5, 10, 15, 20))


result = add(10, 20, 30)
print("Your values:", result)

def student_info(**info):
    for key, value in info.items():
        print(key, ":", value)
student_info(
    name="Atul",
    age=22,
    department="SWE"
)

def student(*marks, **info):
    print("Marks:", marks)
    print("Info:", info)
student(
    80, 75, 90,
    name = "Atul Paul",
    dept = "CIS",
    semester = 3
)

def student_result(*marks, **info):
    total = 0

    for mark in marks:
        total += mark

    print("Name:", info["name"])
    print("Department:", info["dept"])
    print("Total:", total)
student_result(
    80, 90, 70,
    name = "Atul Paul",
    dept = "CIS",
)
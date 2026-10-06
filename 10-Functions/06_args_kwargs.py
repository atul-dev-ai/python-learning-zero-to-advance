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


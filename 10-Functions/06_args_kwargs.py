# *args
def add(*numbers): # ekhane numbers ekto TUPLE. tai ekhane loop chalano jay.
    total = 0
    
    for number in numbers:
        total += number
    
    return total

print(add(10, 20))
print(add(10, 20, 40))
print(add(10, 20 , 30, 40, 50))


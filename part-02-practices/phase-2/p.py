def add (a, b, c):
    return a + b + c

print(add(1, 2, 3))


# *args likhe ei "star" python ke bole 
def nums (*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(nums(1, 2, 3, 4, 5))
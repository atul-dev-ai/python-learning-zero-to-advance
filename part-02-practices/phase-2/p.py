def add (a, b, c):
    return a + b + c

print(add(1, 2, 3))


# *args likhe ei "star" python ke bole je amra onek gula number dite pari, ar oi number gula ke "numbers" variable te store kora hobe. numbers gula ekta tuple hobe, karon *args er maddhome tuple e store hoy.
def nums (*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(nums(1, 2, 3, 4, 5))
print(nums(1, 4, 2, 9, 10))
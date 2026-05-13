#range (start, stop, step)
# range(start, stop)
print(range(1, 100))

# i hocche standard value, i er bodhole a b c d neya jabe
"""
range function ekhane i er moddhe value generate korche
i = 1
i = 2
i = 3
i = 4
i = 5

(1, 6) 6 mane 6 er ag porjonto
"""

"""
`for loop` use kora hoy jokhon ami jani loop koto bar cholbe, ba kono sequence er upor kaj korte chai."""

# Ex 1
for i in range(5):
    print(i)
# ekhane range(5) mane 0 theke 4 porjonto

# ex 2
for a in range(1, 7):
    print(i)
# ekhane range(1, 7) mane 1 theke 6 porjonto

# ex 3 list loop
fruits = ["Apple", "Banan", "Mango"]
for fruit in fruits:
    print(fruit)
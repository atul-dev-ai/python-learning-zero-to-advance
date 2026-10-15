'''
Python provides a standard library containing modules for 
common tasks.
We can import these modules instead of writing the same 
functionality from scratch.
'''

# math module
import math
print(math.sqrt(25)) # sqrt mane 25 er square root

print(math.sqrt(64))

# math.pow()
print(math.pow(2, 3)) # 2**3

# math.ceil()
print(math.ceil(4.2)) # nijer soman ba nearest big integer ane.

# math.floor()
print(math.floor(4.9)) # nijer soman ba nearest small integer ane

# math.factorial()
print(math.factorial(5)) # 1*2*3*4*5

# math.pi
print(math.pi)

# Area of a circle
radius = 7
area = math.pi * pow(radius, 2)
print(radius)
print(area)

# we use "math.pi" for π and pow(radius, 2) to square the radius.
# Multiplying them gives the circle's area.

# random integer
import random
number = random.randint(1, 10)
# randint 1 and 10 duitai include kore.

# random decimal number
print(random.random())

# select random item from List
names = [
    "atul",
    "Ankit",
    "Anik",
    "Karim",
    "Rahim"
]

winner = random.choice(names)
print("Selected:", winner)

# list shuffle
cards = [
    "A",
    "b",
    "C",
    "D",
    "d"
]

random.shuffle(cards)
print(cards)

# present time and date
from datetime import datetime
now = datetime.now()
print(now)

# only date
from datetime import date

todayy = date.today()
print(todayy)
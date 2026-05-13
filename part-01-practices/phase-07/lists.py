"""
list holo ordered collection, jekhane multiple item rakha jay.
numbers = [10, 20, 30, 40, 50]

list er boishisto:
    - ordered
    - **mutable**
    - duplicate thakte pare
    - mixed value thakte pare
    items = [1, "Apple", 3.5, True]

"""

# access
fruits = ["Apple", "Banana", "Mango", "Jack Fruit"]
print(fruits[0])

# change value 
fruits[0] = "Mango"
print(fruits)
fruits.append("Banana")

# remove items
fruits.remove("Banana")
print(fruits)

# length
print(len(fruits))

# loop through list
for fruit in fruits:
    print(fruit)


numbers = {1, 2, 3, 4, 5}

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

print("\n--- Additional Set Methods ---")

num2 = {10, 20, 30}

num2.add(40)
print(num2)

num2.update([40, 50, 60, 70])
print(num2)

num2.discard(20)
print(num2)

num2.remove(30)
print(num2)
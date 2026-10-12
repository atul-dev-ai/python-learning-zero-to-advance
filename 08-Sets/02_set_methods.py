numbers = {1, 2, 3, 4, 5}

# add()
numbers.add(9) # Adding duplicate values leaves the set unchanged.
print(numbers)

# update()
numbers.update([5, 6, 7, 8]) 
print(numbers)

# remove()
numbers.remove(8)
print(numbers)

# discard()
numbers.discard(9) # Removes element if present; does not raise error if absent.
print(numbers)

# pop()
"""Since sets are unordered, you cannot predict which element will be removed."""
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
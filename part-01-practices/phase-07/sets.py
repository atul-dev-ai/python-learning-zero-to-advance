"""
set holo unordered collection of unique items.
boishito:
    - unordered
    - duplicated nai
    - mutable, but item unique thakbe
"""

nums = {1, 2, 3, 3, 4, 9, 9}
print(nums)

nums.add(5)
print(nums)
nums.remove(9)
print(nums)
# print(nums.remove(5))

# union 
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)

# intersection
print (a & b)

# unordered thakleu ordered hoye jay. 
num = [1,2,2,2,3,6, 4, 5, 6,6 ,7,8, 9, 12, 11, 11, 10] # list
s = set(num) # list ke set er bitor pass kora hoiche taile list set hoye geche. tuple o convert kora jay. convert korle duplicate delete hoye jay.
print(s)


'''
map() bebohar kore ekti list/iterable er 
protiti element er upore ekoi function chalano jay.
-> ekoi kaj list er prottek ta item er upore kore.
'''

numbers = [1, 2, 3, 4, 5]
result = []
for number in numbers:
    result.append(number ** 2)

print(result)

results = map(lambda x: x ** 2, numbers)
print(result) # output shorashori list hobe na. Python ekti map object dey.

result1 = list(
    map(lambda c: c **2, numbers)
)
print(result1)

numbers2 = [222, 22, 29, 10, 8]
result2 = list(
    map(lambda d: d ** 2, numbers2)
)
print(result2)

result3 = list (
    map(lambda e: e + 10, numbers2)
)
print(result3)

# names = ["Atul Paul", "Rahim", "Karim"]
# result4 = list(
#     map(lambda f: upper)
# )

'''
filter() selects elements from an iterable based on a condition. 
Only elements for which the function returns True are kept.
'''

numbers3 = [1, 2, 3, 4, 5, 6, 7]
result4 = []
for number in numbers3:
    if number % 2 == 0:
        result4.append(number)
print(result4)

result4 = list(
    filter(lambda x: x % 3 == 0, numbers3)
)
print(result4)

result4 = list(
    filter(lambda x: x > 5, numbers3)
)
print(result4)

odd_numbers = list(
    filter(lambda x: x % 2 != 0, numbers3)
)
print(odd_numbers)


# positive number
numbers4 = [-5, 10, -2, 8, 0, 15, 10, -3, -9, 12]
positive = list(
    filter(lambda x: x > 0, numbers4)
)
print(positive)
print(sorted(positive))

# Negative Numbers
negative = list(
    filter(lambda x: x < 0, numbers4)
)
print(negative)

# Student passed
marks = [35, 80, 45, 90, 25, 70]
passed = list(
    filter(lambda mark: mark >= 40, marks)
)
print(passed)


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


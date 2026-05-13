"""
while loop chole jotokhon condition TRUE thake
"""
# ex
i = 1
while i <= 5:
    print(i)
    i += 1

"""
ekhane i = 1, joto khon i <= 5 mane i 5 er soman ba suto, tarpor i barbe.
jodi i na barano hoy tahole infinite loop cholbe"""

while True:
    print("This will run once or more")
    choice = input("Continue ? (y/n): ")
    if choice == "y":
        break
def introduce(name, age):
    print("Name", name, "Age", age)

introduce("Alice", 30)
introduce(25, "Bob") # ekhane vul ta hocche name parameter e age pass kora hoiche, ar age parameter e name pass kora hoiche. python ekhane nije theke check korteche na je name ta ki age e gelo naki. eta nije ke define kore dite hobe.

# Keyrword Arguments. eta diye parameter name diye value pass kora jay. ekhane prm name ekta dilam arekta dilam na emon dile syntax error ashbe. Jemon:
introduce(age = 21, name = "Atul Paul") # ekhane age parameter e 21 pass kora hoiche, ar name parameter e "Atul Paul" pass kora hoiche. ekhane vul ta hocche na karon ekhane amra parameter name diye value pass korechi.

"""
normanl params: fixed input
args: unlimited unnamed output
kwargs: unlimited named Output
"""
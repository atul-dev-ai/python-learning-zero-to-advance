amount = int(input("Enter total amount: "))

if amount >= 5000:
    print("Eligible for discount")
    print("Enter mode of payment")
    mode = input("A-cash or B-card C-MFS: ")
    if mode == "B":
        print("Discound Applied")
    elif mode == "A" or mode == "C":
        print("Discount not applied")
    else:
        print("In-valid input")

elif (amount > 0) and (amount < 5000):
    print("Not eligible")
else:
    print("Please do shoping something")
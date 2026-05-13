amount = int(input("Enter total amount: "))

if amount >= 5000:
    print("Eligible for discount")
elif (amount > 0) and (amount < 5000):
    print("Not eligible")
else:
    print("Please do shoping something")
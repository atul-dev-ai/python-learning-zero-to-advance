'''
Polymorphism is an OOP Concept in which the same method name or 
interface can produce different behaviors for different objects.
'''
# same method, different behavior
class Dog:
    def sound(self):
        print("Dog says Woof")

class Cat:
    def sound(self):
        print("Cat Says Meow")

class Cow:
    def sound(self):
        print("Cow says Moo!")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()

# loop using polymorphism

class Dog:
    def sound(self):
        print("Woof!")


class Cat:
    def sound(self):
        print("Meow!")


class Cow:
    def sound(self):
        print("Moo!")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()
'''
Polymorphism allows us to write flexible code that works 
with different object types through a common method name.
'''

# payment system sample
class BkashPyament:
    def pay(self, amount):
        print(f"Paid tk {amount} using bkash")

class CardPayment:
    def pay(self, amount):
        print(f"Paid tk {amount} using card")

class BankPayment:
    def pay(self, amount):
        print(f"Paid tk {amount} using Bank Transfer.")

def process_payment(payment_method, amount):
    payment_method.pay(amount)

bkash = BkashPyament()
card = CardPayment()
bank = BankPayment()

process_payment(bkash, 3000)
process_payment(card, 1000)
process_payment(bank, 2000)


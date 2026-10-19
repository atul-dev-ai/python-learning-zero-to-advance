'''
- Abstraction is an OOP concept that exposes essential features while 
hiding unnecessary implementation details.

- Abstraction helps define a common interface and ensures that required methods 
are implemented by concrete classes.

'''

# create abstraction in python
from abc import ABC, abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class BkashPayment(Payment):
    def pay(self, amount):
        print(f"Paid tk {amount} using bkash.")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid tk {amount} using card.")

bkash = BkashPayment()
card = CardPayment()

bkash.pay(1000)
card.pay(2000)


'''
- Abstraction is an OOP concept that exposes essential features while 
hiding unnecessary implementation details.

- Abstraction helps define a common interface and ensures that required methods 
are implemented by concrete classes.

'''

# create abstraction in python
from abc import ABC, abstractmethod

# Creating abstract class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

# method implement to child class
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



# Notification system practice
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print("Email sent:", message)

class SMSNotification(Notification):
    def send(self, message):
        print("SMS send:", message)

Notifications = [
    EmailNotification(),
    SMSNotification()
]

for notification in Notifications:
    notification.send("Your class starts at 8 AM")
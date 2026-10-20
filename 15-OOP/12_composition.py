'''
Composition is an OOP concept in which an object 
contains or uses another object. It represents a has-a relationship.
'''
class Engine:
    def start(self):
        print("Engine Started!")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car is ready to drive!")

car = Car()
car.start()
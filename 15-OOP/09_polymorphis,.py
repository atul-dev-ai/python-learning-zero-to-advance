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

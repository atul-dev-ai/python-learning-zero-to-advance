'''
Inheritance is an OOP feature that allows one class to reuse 
the attributes and methods of another class.
'''


class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog1 = Dog()

dog1.eat()
dog1.bark()

'''
Inheritance reduces code duplication by allowing related classes to share
common attributes and methods.
'''

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_info(self):
        print("Name:", self.name)
        print("Email:", self.email)


class Student(Person):
    def study(self):
        print(self.name, "is studying")


class Teacher(Person):
    def teach(self):
        print(self.name, "is teaching")


student1 = Student("Atul", "atul@example.com")
teacher1 = Teacher("Rahim", "rahim@example.com")

student1.show_info()
student1.study()

print("----------")

teacher1.show_info()
teacher1.teach()



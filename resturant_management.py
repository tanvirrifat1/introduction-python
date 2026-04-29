class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):  # Override parent method
        print("Woof! Woof!")

    def bark(self):
        print("Bark")


class Cat(Animal):
    def sound(self):  # Override parent method
        print("Meow! Meow!")


class Cow(Animal):
    def sound(self):  # Override parent method
        print("Moo! Moo!")


# Polymorphism in action
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()  # Same method, different behavior

d = Dog()
d.sound()
d.bark()

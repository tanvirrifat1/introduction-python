class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Woof!")


dog = Dog("Buddy")


dog.make_sound()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Invalid age")


person = Person("Alice", 30)


person.age = 40
person.name = "Bob"
print(person.age)
print(person.name)

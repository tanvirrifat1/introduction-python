class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(
        self,
        name,
    ):
        super().__init__(name)

    def evalution_exam(self):
        return random.randint(1, 100)

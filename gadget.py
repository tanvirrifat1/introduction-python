class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} costs {self.price}"

    def move(self):
        pass


class Car(Vehicle):
    def __init__(self, name, price, seats):
        self.seats = seats
        super().__init__(name, price)


green_line = Car("Green Line", 30000, 5)
print(green_line)

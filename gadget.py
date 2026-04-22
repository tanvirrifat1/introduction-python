class Gedget:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f"Running  Laptop: {self.brand}"


class Laptop:
    def __init__(self, memory, ssd):
        self.memory = memory
        self.ssd = ssd

    def run(self):
        return f"Running Laptop with {self.memory} and {self.ssd}"

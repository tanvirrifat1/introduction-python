class Laptop:
    def __init__(self, brand, price, color, memory):
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f"Running {self.brand}"

    def coding(self):
        return f"Learning coding on python"

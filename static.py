class Shopping:
    cart = []
    origin = "Dhaka"

    def __init__(self, name, location):
        self.name = "Jamuna Shopping Mall"
        self.location = "Banani"

    def purchase(self, item, price, amount):
        remining = amount - price
        print(f"Purchased {item} for {price}. Remaining balance: {remining}")


Shopping.purchase(Shopping, "Shirt", 500, 1000)

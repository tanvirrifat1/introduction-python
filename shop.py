class Shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)
        print(f"{item} added to cart")


rifat = Shop("rifat")
rifat.add_to_cart("laptop")
rifat.add_to_cart("phone")

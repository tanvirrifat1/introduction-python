class shopping:
    def __init__(
        self,
        name,
    ):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {"item": item, "price": price, "quantity": quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total = total + (item["price"] * item["quantity"])
        print(f"Total amount: {total}")
        if amount < total:
            print("Insufficient funds.")
        else:
            change = amount - total
            print(f"Change: {change}")


rifat = shopping("rifat")
rifat.add_to_cart("laptop", 100110, 1)
rifat.add_to_cart("mouse", 50, 2)
rifat.checkout(10000)

print(rifat.cart)

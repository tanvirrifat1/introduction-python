from abc import ABC


class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = None

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name):
        item = restaurant.menu.find_item(item_name)
        if item:
            pass
        else:
            print(f"Item not found: {item_name}")

    def view_cart(self):
        print("Cart Items:")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
            print(f"Total Price: {self.cart.total_price}")


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity

    def remove(self, item):
        if item in self.items:
            del self.items[item]


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


emp = Employee("Rohit", 1234567890, "i2wYr@example.com", "Pune", 25, "Manager", 50000)


class Admin(User):
    def __init__(
        self,
        name,
        phone,
        email,
        address,
    ):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employees(self, restaurant):
        restaurant.view_employees()

    def add_new_iteam(self, restaurant, item):
        restaurant.menu.add_item(item)

    def remove_iteam(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)


class Restaurant:

    def __init__(
        self,
        name,
    ):
        self.name = name
        self.employees = []
        self.menu = FoodItem()

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee added successfully: {employee.name}")

    def view_employees(self):
        for emp in self.employees:
            print(
                emp.name,
                emp.email,
                emp.phone,
                emp.address,
                emp.age,
                emp.designation,
                emp.salary,
            )


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def find_item(self, Item_name):
        for item in self.items:
            if item.name == Item_name:
                return item
        return None

    def remove_item(self, Item_name):
        item = self.find_item(Item_name)
        if item:
            self.items.remove(item)
            print(f"Item removed successfully: {item.name}")
        else:
            print(f"Item not found: {Item_name}")

    def show_menu(self):
        print("Menu Items:")
        for item in self.items:
            print(f"{item.name} - Price: {item.price}, Quantity: {item.quantity}")


class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


mn = Menu()
item1 = FoodItem("Pizza", 10, 5)
mn.add_item(item1)
item2 = FoodItem("Burger", 5, 10)
mn.add_item(item2)

print("Menu Items:")
for item in mn.items:
    print(f"{item.name} - Price: {item.price}, Quantity: {item.quantity}")

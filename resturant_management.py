from abc import ABC


class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


emp = Employee("Rohit", 1234567890, "i2wYr@example.com", "Pune", 25, "Manager", 50000)


class Admin(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.employees = []

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employees(self, restaurant):
        restaurant.view_employees()


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employees(self):
        for employee in self.employees:
            print(employee.name)


class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)

    def fined_menu_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.fined_menu_item(item_name)

        if item:
            self.items.remove(item)
            print(f"{item_name} removed from menu.")
        else:
            print(f"{item_name} not found in menu.")

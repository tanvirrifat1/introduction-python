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

    def add_employee(self, name, email, phone, address, age, designation, salary):
        emply = Employee(name, email, phone, address, age, designation, salary)
        self.employees.append(emply)
        print(f"Employee added successfully ${emply.name}")

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


ad = Admin("Rohit", 1234567890, "i2wYr@example.com", "Pune", 25, "Manager", 50000)
ad.add_employee("Rohit", 1234567890, "i2wYr@example.com", "Pune", 25, "Manager", 50000)
ad.view_employees()

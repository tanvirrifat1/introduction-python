class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats = self.booked_seats + 1
            return True
        return False


# bus1 = Bus(10, "Dhaka to Chittagong", 50)
# print(bus1.available_seats())
# print(bus1.book_seat())
# print(bus1.available_seats())
# print(bus1.book_seat())
# print(bus1.available_seats())


class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus


class Admin:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            return True
        return False


# admin1 = Admin("admin", "1234")
# print(admin1.login("admin", "1234"))

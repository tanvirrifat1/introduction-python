from datetime import datetime


class RideSharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_diver(self, diver):
        self.drivers.append(diver)

    def __str__(self):
        return f"Company Name: {self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}"


class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.diver = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_diver(self, diver):
        self.diver = diver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.diver.wallet += self.estimated_fare

    def __repr__(self):
        return f"Ride from {self.start_location} to {self.end_location}"


class RideRequest:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location

    def find_diver(self, ride_request):
        if len(self.available_divers) > 0:
            print("Looking for divers...")
            diver = self.available_divers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            diver.accept_rider(ride)
            return diver

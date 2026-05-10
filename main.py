from ride import Ride, RideSharing, RideRequest
from vehicle import Car, Bike
from user import Driver, Rider

niye_jau = RideSharing(
    "Niye Jau",
)

rahim = Rider("Rahim", "rahim@123", 123456, "Dhaka", 1000)
niye_jau.add_rider(rahim)

kolimuddin = Driver("Kolimuddin", "kolimuddin@123", 123456, "Dhaka")
niye_jau.add_driver(kolimuddin)

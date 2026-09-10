from parking_lot import ParkingLot
from parking_floor import ParkingFloor
from parking_spot import ParkingSpot
from vehicle_size import VehicleSize
from bike import Bike
from car import Car
from truck import Truck

# Setup
lot = ParkingLot("City Parking")

floor1 = ParkingFloor(1)
floor1.add_spot(ParkingSpot("F1-S1", VehicleSize.SMALL))
floor1.add_spot(ParkingSpot("F1-M1", VehicleSize.MEDIUM))
floor1.add_spot(ParkingSpot("F1-L1", VehicleSize.LARGE))

floor2 = ParkingFloor(2)
floor2.add_spot(ParkingSpot("F2-M1", VehicleSize.MEDIUM))
floor2.add_spot(ParkingSpot("F2-M2", VehicleSize.MEDIUM))

lot.add_floor(floor1)
lot.add_floor(floor2)

# Park vehicles
print("--- Parking vehicles ---")
bike = Bike("B-123")
car = Car("C-456")
truck = Truck("T-789")

lot.park_vehicle(bike)
lot.park_vehicle(car)
lot.park_vehicle(truck)

# Show availability
print("\n--- Availability ---")
floor1.display_availability()
floor2.display_availability()

# Unpark
print("\n--- Unparking ---")
lot.unpark_vehicle("C-456")

print("\n--- Availability after unpark ---")
floor1.display_availability()

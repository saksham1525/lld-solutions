import time
from vehicle import Vehicle
from parking_spot import ParkingSpot

class ParkingTicket:
    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = time.time()
        self.exit_time = None

    def mark_exit(self):
        self.exit_time = time.time()

    def duration_hours(self) -> float:
        end = self.exit_time or time.time()
        return (end - self.entry_time) / 3600

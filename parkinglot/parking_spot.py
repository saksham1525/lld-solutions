from vehicle import Vehicle
from vehicle_size import VehicleSize

class ParkingSpot:
    def __init__(self, spot_id: str, spot_size: VehicleSize):
        self.spot_id = spot_id
        self.spot_size = spot_size
        self.is_occupied = False
        self.parked_vehicle = None

    def park_vehicle(self, vehicle: Vehicle):
        self.parked_vehicle = vehicle
        self.is_occupied = True

    def unpark_vehicle(self):
        self.parked_vehicle = None
        self.is_occupied = False

    def can_fit_vehicle(self, vehicle: Vehicle) -> bool:
        if self.is_occupied:
            return False
        return vehicle.size == self.spot_size

from parking_spot import ParkingSpot
from vehicle import Vehicle

class ParkingFloor:
    def __init__(self, floor_number: int):
        self.floor_number = floor_number
        self.spots: list[ParkingSpot] = []

    def add_spot(self, spot: ParkingSpot):
        self.spots.append(spot)

    def find_available_spot(self, vehicle: Vehicle):
        for spot in self.spots:
            if spot.can_fit_vehicle(vehicle):
                return spot
        return None

    def display_availability(self):
        print(f"Floor {self.floor_number}")
        for spot in self.spots:
            status = "occupied" if spot.is_occupied else "free"
            print(f"Spot {spot.spot_id} ({spot.spot_size.value}): {status}")

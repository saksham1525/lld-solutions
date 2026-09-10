from parking_floor import ParkingFloor
from parking_ticket import ParkingTicket
from vehicle import Vehicle

RATE_PER_HOUR = 10.0

class ParkingLot:
    def __init__(self, name: str):
        self.name = name
        self.floors: list[ParkingFloor] = []
        self.active_tickets: dict[str, ParkingTicket] = {}  # license -> ticket

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def park_vehicle(self, vehicle: Vehicle):
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle)
            if spot:
                spot.park_vehicle(vehicle)
                ticket = ParkingTicket(vehicle, spot)
                self.active_tickets[vehicle.license_number] = ticket
                print(f"{vehicle.license_number} parked at spot {spot.spot_id}")
                return ticket
        print(f"No available spot for {vehicle.license_number}")
        return None

    def unpark_vehicle(self, license_number: str):
        ticket = self.active_tickets.pop(license_number, None)
        if ticket is None:
            print(f"No active ticket for {license_number}")
            return None
        ticket.mark_exit()
        ticket.spot.unpark_vehicle()
        fee = max(1, ticket.duration_hours()) * RATE_PER_HOUR
        print(f"{license_number} left spot {ticket.spot.spot_id}. Fee: ${fee:.2f}")
        return fee

# Designing a Parking Lot System

## Requirements
1. The parking lot has multiple floors, each floor with a number of parking spots.
2. The parking lot supports different types of vehicles: bikes, cars, and trucks.
3. Each parking spot has a size (SMALL, MEDIUM, LARGE) and can fit a vehicle whose size is less than or equal to the spot's size.
4. The system assigns a spot to a vehicle on entry (issuing a ticket) and frees the spot on exit.
5. The system can report, per floor, which spots are occupied/free.
6. On exit, a parking fee is calculated from the parked duration.

## Classes and Enumerations
1. **VehicleSize** (`vehicle_size.py`) — enum: `SMALL`, `MEDIUM`, `LARGE`.
2. **Vehicle** (`vehicle.py`) — abstract base class storing `license_number` and `size`. Extended by `Car`, `Bike`, and `Truck` (each fixes its own `VehicleSize`).
3. **ParkingSpot** (`parking_spot.py`) — tracks `spot_id`, `spot_size`, occupancy, and the parked vehicle. `can_fit_vehicle` checks the spot is free and large enough.
4. **ParkingTicket** (`parking_ticket.py`) — records the vehicle, spot, entry time, and exit time; `duration_hours` computes elapsed time for billing.
5. **ParkingFloor** (`parking_floor.py`) — holds a list of `ParkingSpot`s for one floor. `find_available_spot` returns the first spot that fits a vehicle; `display_availability` prints each spot's status.
6. **ParkingLot** (`parking_lot.py`) — holds a list of `ParkingFloor`s and a map of active `ParkingTicket`s keyed by license number. `park_vehicle` scans floors in order for the first available spot; `unpark_vehicle` closes the ticket, frees the spot, and computes the fee (`RATE_PER_HOUR = 10.0`, minimum 1 hour billed).
7. **parking_lot_demo.py** — sets up a lot with two floors, parks a bike/car/truck, prints availability, then unparks a vehicle and shows the fee.

## Running the demo
```
python parking_lot_demo.py
```

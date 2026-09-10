# Python Basics for LLD — Using the Parking Lot as the Example

Every concept below is pulled directly from the files in this folder. Read them side by side.

---

## 1. Classes and `__init__`

A **class** is a blueprint. `__init__` is the constructor — it runs automatically when you create an object.

```python
# parking_spot.py
class ParkingSpot:
    def __init__(self, spot_id: str, spot_size: VehicleSize):
        self.spot_id = spot_id        # instance variable
        self.spot_size = spot_size    # instance variable
        self.is_occupied = False      # default value, no argument needed
        self.parked_vehicle = None
```

- `self` is the object itself. Every method gets it as the first argument.
- `self.x = y` stores `y` as a property on this specific object instance.
- You call it like: `spot = ParkingSpot("F1-S1", VehicleSize.SMALL)` — Python passes `self` automatically, you don't pass it manually.

---

## 2. `super().__init__()` — calling the parent constructor

When a class **inherits** from another, `super()` lets you call the parent's `__init__` so parent setup still happens.

```python
# vehicle.py  — the PARENT
class Vehicle(ABC):
    def __init__(self, license_number: str, size: VehicleSize):
        self.license_number = license_number
        self.size = size

# car.py  — the CHILD
class Car(Vehicle):
    def __init__(self, license_number: str):
        super().__init__(license_number, VehicleSize.MEDIUM)
        #       ^^^^ calls Vehicle.__init__ with these args
```

Without `super().__init__(...)`, `self.license_number` and `self.size` would never get set, and every method inherited from `Vehicle` would break.

Rule of thumb: **always call `super().__init__(...)` as the first line of a child's `__init__`**.

---

## 3. Inheritance — `class Child(Parent)`

```python
class Car(Vehicle):   # Car IS-A Vehicle
    ...
```

`Car` inherits everything defined in `Vehicle` (its methods and variables). You can then:
- **Use** inherited methods as-is.
- **Override** them by redefining the method in the child.
- **Extend** them by calling `super().method()` and then adding more logic.

In this project the hierarchy looks like:

```
Vehicle (abstract)
├── Car
├── Bike
└── Truck
```

---

## 4. `ABC` and `@abstractmethod` — Abstract Classes

`ABC` = Abstract Base Class. It lets you define a **contract**: "every subclass MUST implement these methods."

```python
# vehicle.py
from abc import ABC

class Vehicle(ABC):       # Vehicle is abstract — you can't do Vehicle("X", SIZE)
    ...
```

```python
# fee_strategy.py
from abc import ABC, abstractmethod

class FeeStrategy(ABC):
    @abstractmethod                               # <-- must be implemented by subclasses
    def calculate_fee(self, ticket) -> float:
        pass                                      # no body needed here

class FlatRateFeeStrategy(FeeStrategy):
    def calculate_fee(self, ticket) -> float:     # concrete implementation
        ...
```

If a subclass forgets to implement an `@abstractmethod`, Python raises a `TypeError` when you try to instantiate it. This is how Python enforces **interfaces** — a concept central to LLD.

---

## 5. `Enum` — Named Constants

An `Enum` is a set of named, fixed values. Great for things that have a limited, well-known set of options.

```python
# vehicle_size.py
from enum import Enum

class VehicleSize(Enum):
    SMALL  = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE  = "LARGE"
```

Usage:

```python
spot_size = VehicleSize.SMALL
vehicle.get_size() == VehicleSize.MEDIUM   # comparison works cleanly
```

Why not just use plain strings like `"SMALL"`? Because:
- Typos like `"smal"` are silent bugs; `VehicleSize.SMAL` raises `AttributeError` immediately.
- IDEs can autocomplete enum members.
- You can iterate over all values: `for size in VehicleSize: ...`

---

## 6. `@staticmethod` — Methods that don't need `self`

A `@staticmethod` belongs to the class but doesn't receive `self` (no access to instance data). Use it when the logic is related to the class but doesn't depend on any specific object.

```python
# parking_lot.py
class ParkingLot:
    _instance = None                  # class-level variable

    @staticmethod
    def get_instance():               # no 'self' parameter
        if ParkingLot._instance is None:
            ParkingLot._instance = ParkingLot()
        return ParkingLot._instance
```

```python
# parking_lot_demo.py
class ParkingLotDemo:
    @staticmethod
    def main():
        parking_lot = ParkingLot.get_instance()   # called on the class, not an object
        ...

if __name__ == "__main__":
    ParkingLotDemo.main()
```

Called as `ClassName.method()` — no object needed.

---

## 7. Singleton Pattern — only one instance ever

The `ParkingLot` uses the **Singleton** design pattern: only one `ParkingLot` object should exist in the whole program.

```python
class ParkingLot:
    _instance = None           # class variable — shared across all instances
    _lock = threading.Lock()   # for thread safety

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        # ... setup ...

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            with ParkingLot._lock:
                if ParkingLot._instance is None:        # double-checked locking
                    ParkingLot._instance = ParkingLot()
        return ParkingLot._instance
```

Always get the parking lot via `ParkingLot.get_instance()`, never via `ParkingLot()` directly.

---

## 8. Type Hints — `str`, `int`, `List`, `Dict`, `Optional`

Python is dynamically typed but you can **annotate** types for readability and IDE support.

```python
from typing import List, Dict, Optional

def park_vehicle(self, vehicle: Vehicle) -> Optional[ParkingTicket]:
    ...

floors: List[ParkingFloor] = []
active_tickets: Dict[str, ParkingTicket] = {}
```

| Hint | Meaning |
|------|---------|
| `str` | a string |
| `int` | an integer |
| `float` | a decimal number |
| `bool` | True or False |
| `List[X]` | a list where every element is type X |
| `Dict[K, V]` | a dict with key type K and value type V |
| `Optional[X]` | either type X or `None` |

These are just hints — Python doesn't enforce them at runtime. But they make LLD code much easier to read and reason about.

---

## 9. Class Variables vs Instance Variables

```python
class FlatRateFeeStrategy(FeeStrategy):
    RATE_PER_HOUR = 10.0           # class variable — shared by ALL instances

    def calculate_fee(self, ticket):
        return hours * self.RATE_PER_HOUR   # accessed via self (or ClassName.RATE_PER_HOUR)
```

```python
class ParkingSpot:
    def __init__(self, spot_id, spot_size):
        self.spot_id = spot_id     # instance variable — unique to each ParkingSpot object
```

- **Class variable**: defined at class level, outside any method. One copy, shared by all objects.
- **Instance variable**: defined inside `__init__` using `self.`. Each object has its own copy.

---

## 10. `with` statement — Context Managers (used for locks)

```python
import threading

class ParkingSpot:
    def __init__(self, ...):
        self._lock = threading.Lock()

    def park_vehicle(self, vehicle):
        with self._lock:            # acquires the lock on entry, releases on exit (even if error)
            self.parked_vehicle = vehicle
            self.is_occupied = True
```

`with` guarantees cleanup. For a lock, this means: if an exception happens inside the block, the lock is still released — no deadlock. You'll also see it with files: `with open("file.txt") as f:`.

---

## 11. List Comprehensions — compact loops

```python
# parking_floor.py
available_spots = [
    spot for spot in self.spots.values()
    if not spot.is_occupied_spot() and spot.can_fit_vehicle(vehicle)
]
```

This is equivalent to:

```python
available_spots = []
for spot in self.spots.values():
    if not spot.is_occupied_spot() and spot.can_fit_vehicle(vehicle):
        available_spots.append(spot)
```

The comprehension form is more Pythonic and reads almost like English: "all spots where the spot is not occupied and can fit the vehicle."

---

## 12. `Dict` and common dict methods

```python
# parking_lot.py
self.active_tickets: Dict[str, ParkingTicket] = {}

# add / update
self.active_tickets[vehicle.get_license_number()] = ticket

# remove and get (returns None if key missing, no KeyError)
ticket = self.active_tickets.pop(license_number, None)
```

| Operation | Syntax |
|-----------|--------|
| Set a key | `d[key] = value` |
| Get a value | `d[key]` (raises KeyError if missing) |
| Get with default | `d.get(key, default)` |
| Remove and return | `d.pop(key, default)` |
| Iterate values | `for v in d.values()` |
| Iterate keys | `for k in d.keys()` |
| Iterate both | `for k, v in d.items()` |

---

## 13. `defaultdict` — dict with auto-default values

```python
from collections import defaultdict

# parking_floor.py
available_counts = defaultdict(int)   # any missing key returns 0 automatically

for spot in self.spots.values():
    if not spot.is_occupied_spot():
        available_counts[spot.get_spot_size()] += 1   # no KeyError even on first access
```

Without `defaultdict`, you'd need: `available_counts[key] = available_counts.get(key, 0) + 1`.

---

## 14. Lambda — tiny inline functions

```python
# parking_floor.py
available_spots.sort(key=lambda x: x.get_spot_size().value)
```

`lambda x: expression` is an anonymous (nameless) function. Here it says: "sort the list, and for each element `x`, use `x.get_spot_size().value` as the sort key."

Equivalent full function:
```python
def get_sort_key(x):
    return x.get_spot_size().value

available_spots.sort(key=get_sort_key)
```

---

## 15. f-strings — string formatting

```python
print(f"Vehicle {vehicle.get_license_number()} parked at spot {spot.get_spot_id()}")
print(f"Car C-456 unparked. Fee: ${fee:.2f}")   # :.2f = 2 decimal places
```

Anything inside `{}` is evaluated as Python. Far cleaner than `"Vehicle " + vehicle.get_license_number() + " parked..."`.

---

## 16. `if __name__ == "__main__":`

```python
# parking_lot_demo.py
if __name__ == "__main__":
    ParkingLotDemo.main()
```

When Python runs a file directly, `__name__` is `"__main__"`. When that file is imported by another file, `__name__` is the module name. This guard means: "only run this block if I'm the entry point, not if I'm imported." Standard way to write runnable scripts that are also importable.

---

## The LLD Design Patterns visible in this project

| Pattern | Where | What it does |
|---------|-------|-------------|
| **Singleton** | `ParkingLot` | Only one parking lot instance exists |
| **Strategy** | `FeeStrategy`, `ParkingStrategy` | Swap algorithms at runtime without changing the caller |
| **Abstract class / Interface** | `Vehicle`, `FeeStrategy`, `ParkingStrategy` | Enforce a contract on subclasses |
| **Factory (light)** | `Car`, `Bike`, `Truck` constructors | Each vehicle type hardcodes its own size |

---

## Quick Reference — symbols at a glance

| Symbol | Meaning |
|--------|---------|
| `class Foo:` | define a class |
| `class Foo(Bar):` | Foo inherits from Bar |
| `def __init__(self, ...):` | constructor |
| `self.x` | instance variable / attribute |
| `super().__init__(...)` | call parent constructor |
| `class Foo(ABC):` | abstract class (can't instantiate directly) |
| `@abstractmethod` | subclasses MUST implement this method |
| `@staticmethod` | method that doesn't receive `self` |
| `class Size(Enum):` | enum of named constants |
| `Optional[X]` | value can be X or None |
| `List[X]` | list of X |
| `Dict[K, V]` | dictionary |
| `with lock:` | context manager — auto cleanup |
| `[x for x in items if cond]` | list comprehension |
| `lambda x: expr` | anonymous function |
| `f"text {var}"` | formatted string |
| `if __name__ == "__main__":` | entry point guard |

from typing import Dict, Optional
from money import Money
from item import Item
from states import VendingMachineState, IdleState

class VendingMachine:
    def __init__(self):
        self.items: Dict[str, Item] = {}
        self.current_state = IdleState(self)
        self.selected_item_code = None

    # --- Public API, called by the outside world, in transaction order ---

    def add_item(self, code: str, name: str, price: int, quantity: int) -> Item:
        item = Item(code, name, price, quantity)
        self.items[code] = item
        return item

    def select_item(self, code: str) -> None:
        self.current_state.select_item(code)

    def insert_money(self, money: Money) -> None:
        self.current_state.insert_money(money)

    def dispense(self) -> None:
        self.current_state.dispense()

    # --- Inventory lookups ---

    def get_item(self, code: str) -> Optional[Item]:
        return self.items.get(code)

    def is_available(self, code: str) -> bool:
        item = self.get_item(code)
        return item is not None and item.is_available()

    # --- Internals used by VendingMachineState subclasses ---

    def get_selected_item(self) -> Item:
        return self.get_item(self.selected_item_code)

    def set_selected_item_code(self, code: str) -> None:
        self.selected_item_code = code

    def set_state(self, state: VendingMachineState) -> None:
        self.current_state = state

    def reset(self) -> None:
        self.selected_item_code = None
        self.set_state(IdleState(self))

    def dispense_item(self) -> None:
        item = self.get_item(self.selected_item_code)
        item.reduce_stock()
        print(f"Dispensed: {item.get_name()}")
        self.reset()

from typing import Dict, Optional
from currency import Currency
from item import Item
from states import VendingMachineState, IdleState

class VendingMachine:
    def __init__(self):
        self.items: Dict[str, Item] = {}
        self.current_state = IdleState(self)
        self.balance = 0
        self.selected_item_code = None

    def insert_coin(self, currency: Currency) -> None:
        self.current_state.insert_coin(currency)

    def add_item(self, code: str, name: str, price: int, quantity: int) -> Item:
        item = Item(code, name, price, quantity)
        self.items[code] = item
        return item

    def is_available(self, code: str) -> bool:
        item = self.get_item(code)
        return item is not None and item.is_available()

    def get_item(self, code: str) -> Optional[Item]:
        return self.items.get(code)

    def select_item(self, code: str) -> None:
        self.current_state.select_item(code)

    def dispense(self) -> None:
        self.current_state.dispense()

    def dispense_item(self) -> None:
        item = self.get_item(self.selected_item_code)
        if self.balance >= item.get_price():
            item.reduce_stock()
            self.balance -= item.get_price()
            print(f"Dispensed: {item.get_name()}")
            if self.balance > 0:
                print(f"Returning change: ₹{self.balance}")
        self.reset()
        self.set_state(IdleState(self))

    def reset(self) -> None:
        self.selected_item_code = None
        self.balance = 0

    def add_balance(self, value: int) -> None:
        self.balance += value

    def get_selected_item(self) -> Item:
        return self.get_item(self.selected_item_code)

    def set_selected_item_code(self, code: str) -> None:
        self.selected_item_code = code

    def set_state(self, state: VendingMachineState) -> None:
        self.current_state = state

    def get_balance(self) -> int:
        return self.balance

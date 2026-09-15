from abc import ABC, abstractmethod
from money import Money


class VendingMachineState(ABC):
    """Abstract base class for all vending machine states."""

    def __init__(self, machine):
        self.machine = machine
    
    @abstractmethod
    def insert_money(self, money: Money):
        """Handle money insertion."""
        pass
    
    @abstractmethod
    def select_item(self, code: str):
        """Handle item selection."""
        pass
    
    @abstractmethod
    def dispense(self):
        """Handle dispense request."""
        pass


class IdleState(VendingMachineState):
    """State when machine is waiting for user interaction."""
    
    def insert_money(self, money: Money):
        print("Please select an item before inserting money.")
    
    def select_item(self, code: str):
        if not self.machine.is_available(code):
            print("Item not available.")
            return
        
        self.machine.set_selected_item_code(code)
        self.machine.set_state(ItemSelectedState(self.machine))
        print(f"Item selected: {code}")
    
    def dispense(self):
        print("No item selected.")


class ItemSelectedState(VendingMachineState):
    """State when an item has been selected but insufficient money inserted."""
    
    def insert_money(self, money: Money):
        price = self.machine.get_selected_item().get_price()
        value = money.get_value()

        if value != price:
            print(f"Add Exactly ₹{price}")
        else:
            print("Exact amount received.")
            self.machine.set_state(HasMoneyState(self.machine))
    
    def select_item(self, code: str):
        print("Item already selected. Please insert money to select a different item.")

    def dispense(self):
        print("Please insert sufficient money.")


class HasMoneyState(VendingMachineState):
    """State when sufficient money has been inserted."""
    
    def insert_money(self, money: Money):
        print("Exact amount paid. No more money accepted.")
    
    def select_item(self, code: str):
        print("Item already selected. Please dispense to select a different item.")

    def dispense(self):
        self.machine.set_state(DispensingState(self.machine))
        self.machine.dispense_item()


class DispensingState(VendingMachineState):
    """State when item is being dispensed - blocks all user input."""
    
    def insert_money(self, money: Money):
        print("Currently dispensing. Please wait.")
    
    def select_item(self, code: str):
        print("Currently dispensing. Please wait.")
    
    def dispense(self):
        # Already triggered by HasMoneyState
        print("Dispensing in progress...")

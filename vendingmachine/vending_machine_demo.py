from vending_machine import VendingMachine
from money import Money

class VendingMachineDemo:
    @staticmethod
    def main():
        vending_machine = VendingMachine()

        # Add products to the inventory (prices in ₹)
        vending_machine.add_item("A1", "Coke", 20, 3)
        vending_machine.add_item("A2", "Pepsi", 20, 2)
        vending_machine.add_item("B1", "Water", 10, 5)

        # Select a product
        print("\n--- Step 1: Select an item ---")
        vending_machine.select_item("A1")

        # Insert exact coin
        print("\n--- Step 2: Insert exact coin ---")
        vending_machine.insert_money(Money.TWENTY)  # ₹20, price is ₹20

        # Dispense the product
        print("\n--- Step 3: Dispense item ---")
        vending_machine.dispense()  # Should dispense Coke

        # Select another item
        print("\n--- Step 4: Select another item ---")
        vending_machine.select_item("B1")

        # Try to overpay
        print("\n--- Step 5: Insert more than needed (should be rejected) ---")
        vending_machine.insert_money(Money.TWENTY)  # ₹20, price is ₹10

        # Try to underpay
        print("\n--- Step 6: Insert less than needed (should be rejected) ---")
        vending_machine.insert_money(Money.FIVE)  # ₹5, price is ₹10

        # Insert exact amount
        print("\n--- Step 7: Insert exact amount ---")
        vending_machine.insert_money(Money.TEN)  # ₹10

        # Dispense the product
        print("\n--- Step 8: Dispense item ---")
        vending_machine.dispense()


if __name__ == "__main__":
    VendingMachineDemo.main()

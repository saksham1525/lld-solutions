# Designing a Vending Machine

## Requirements
1. The machine stocks multiple items, each with a code, name, price, and quantity.
2. A user selects one item at a time; a second item can't be selected mid-transaction.
3. Payment must be a single coin that exactly matches the item's price — no change, no partial payment.
4. On exact payment, the item is dispensed and its stock reduced by one.

## Classes and Enumerations
1. **Money** (`money.py`) — enum of coin/note denominations with `get_value()`.
2. **Item** (`item.py`) — `code`, `name`, `price`, `quantity`; `is_available()` and `reduce_stock()`.
3. **VendingMachineState** (`states.py`) — abstract base defining `insert_money`, `select_item`, `dispense`.
4. **IdleState, ItemSelectedState, HasMoneyState, DispensingState** (`states.py`) — the concrete states: nothing selected → waiting for exact coin/note → exact amount received → dispensing.
5. **VendingMachine** (`vending_machine.py`) — holds the item inventory and delegates actions to whichever state is `current_state`.
6. **VendingMachineDemo** (`vending_machine_demo.py`) — selects an item, pays exact, dispenses; then shows a rejected overpay/underpay before a successful second purchase.

## Simplifications made in this implementation
- No change or partial payment — one coin/note must exactly match the price (an unpayable price, e.g. ₹15, can never be dispensed).
- No refund flow.
- No concurrency handling — `DispensingState` is for clarity, not thread safety.

## Running the demo
```
python vending_machine_demo.py
```

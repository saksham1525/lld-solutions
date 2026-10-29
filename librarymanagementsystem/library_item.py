from datetime import date
from loan import Loan
from member import Member
from states import ItemState, AvailableState

class LibraryItem:
    """A single physical book/magazine."""

    def __init__(self, item_id: str, title: str, author: str):
        self.id = item_id
        self.title = title
        self.author = author
        # A new item is always on the shelf, so it starts in AvailableState.
        # We pass self so the state knows which item it belongs to.
        self.current_state: ItemState = AvailableState(self)
        self.current_loan: Loan | None = None

    # --- Public API ---
    # checkout and return_item don't have any logic here.
    # They just pass the call to the current state, which decides what to do.

    def checkout(self, member: Member) -> None:
        self.current_state.checkout(member)

    def return_item(self, today: date) -> None:
        self.current_state.return_item(today)

    # current_loan is None when the item is available, and a Loan when it is checked out
    def is_available(self) -> bool:
        return self.current_loan is None

    # --- Internals used by the states (AvailableState / CheckedOutState) ---
    # The states decide WHEN something should happen.
    # These methods do the actual work, so the state classes stay small.

    def set_state(self, state: ItemState) -> None:
        self.current_state = state

    # Creates a loan for this item and member, and adds it to the member's loans.
    # No checkout date is passed because Loan sets it to today on its own.
    def start_loan(self, member: Member) -> Loan:
        self.current_loan = Loan(self, member)
        member.add_loan(self.current_loan)
        return self.current_loan

    # Removes the loan from the member's loans and clears it from this item
    def end_loan(self) -> Loan:
        loan = self.current_loan
        loan.member.remove_loan(loan)
        self.current_loan = None
        return loan

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
        self.current_state: ItemState = AvailableState(self)
        self.current_loan: Loan | None = None

    # --- Public API ---

    # checkout & return_item pass the call to current state
    def checkout(self, member: Member) -> None:
        self.current_state.checkout(member)

    def return_item(self, today: date) -> None:
        self.current_state.return_item(today)

    # current_loan is None when the item is available, and a Loan when it is checked out
    def is_available(self) -> bool:
        return self.current_loan is None

    # --- Internals used by the states (AvailableState / CheckedOutState) ---

    def set_state(self, state: ItemState) -> None:
        self.current_state = state

    def start_loan(self, member: Member) -> Loan:
        self.current_loan = Loan(self, member)
        member.add_loan(self.current_loan)
        return self.current_loan

    def end_loan(self) -> Loan:
        loan = self.current_loan
        loan.member.remove_loan(loan)
        self.current_loan = None
        return loan

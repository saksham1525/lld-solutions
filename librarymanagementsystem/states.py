from abc import ABC, abstractmethod
from datetime import date
from member import Member, MAX_BOOKS_PER_MEMBER


class ItemState(ABC):
    """Abstract base class for all library item states."""

    def __init__(self, item):
        self.item = item

    @abstractmethod
    def checkout(self, member: Member):
        """Handle checkout request."""
        pass

    @abstractmethod
    def return_item(self, today: date):
        """Handle return request."""
        pass


class AvailableState(ItemState):
    """State when the item is on the shelf."""

    def checkout(self, member: Member):
        if not member.can_borrow():
            print(f"{member.name} has reached the limit of {MAX_BOOKS_PER_MEMBER} books.")
            return

        loan = self.item.start_loan(member)
        self.item.set_state(CheckedOutState(self.item))
        print(f"'{self.item.title}' checked out by {member.name}, due {loan.due_date}")

    def return_item(self, today: date):
        print(f"'{self.item.title}' is not checked out.")


class CheckedOutState(ItemState):
    """State when the item is on loan to a member."""

    def checkout(self, member: Member):
        print(f"'{self.item.title}' is already checked out.")

    def return_item(self, today: date):
        loan = self.item.end_loan()
        self.item.set_state(AvailableState(self.item))
        print(f"'{self.item.title}' returned by {loan.member.name}. Fine: {loan.fine(today)}")

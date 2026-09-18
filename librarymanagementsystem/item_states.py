from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from loan import Loan

if TYPE_CHECKING:
    from book_copy import BookCopy
    from member import Member

class ItemState(ABC):
    @abstractmethod
    def checkout(self, book_copy: 'BookCopy', member: 'Member') -> None:
        pass

    @abstractmethod
    def return_item(self, book_copy: 'BookCopy') -> None:
        pass

    @abstractmethod
    def place_hold(self, book_copy: 'BookCopy', member: 'Member') -> None:
        pass


def _start_loan(book_copy: 'BookCopy', member: 'Member') -> None:
    loan = Loan(book_copy, member)
    book_copy.current_loan = loan
    member.add_loan(loan)
    book_copy.set_state(CheckedOutState())


class AvailableState(ItemState):
    def checkout(self, book_copy: 'BookCopy', member: 'Member') -> None:
        _start_loan(book_copy, member)
        print(f"{book_copy.get_id()} checked out by {member.get_name()}")

    def return_item(self, book_copy: 'BookCopy') -> None:
        print("Cannot return an item that is already available.")

    def place_hold(self, book_copy: 'BookCopy', member: 'Member') -> None:
        print("Cannot place hold on an available item. Please check it out.")


class CheckedOutState(ItemState):
    def checkout(self, book_copy: 'BookCopy', member: 'Member') -> None:
        print(f"{book_copy.get_id()} is already checked out.")

    def return_item(self, book_copy: 'BookCopy') -> None:
        loan = book_copy.current_loan
        book_copy.current_loan = None
        loan.get_member().remove_loan(loan)
        print(f"{book_copy.get_id()} returned.")

        # If someone is waiting, move to OnHold instead of Available and notify them.
        if book_copy.get_item().has_observers():
            book_copy.set_state(OnHoldState())
            book_copy.get_item().notify_observers()
        else:
            book_copy.set_state(AvailableState())

    def place_hold(self, book_copy: 'BookCopy', member: 'Member') -> None:
        book_copy.get_item().add_observer(member)
        print(f"{member.get_name()} placed a hold on '{book_copy.get_item().get_title()}'")


class OnHoldState(ItemState):
    def checkout(self, book_copy: 'BookCopy', member: 'Member') -> None:
        # Only the member who placed the hold can check it out.
        if book_copy.get_item().is_observer(member):
            _start_loan(book_copy, member)
            book_copy.get_item().remove_observer(member)
            print(f"Hold fulfilled. {book_copy.get_id()} checked out by {member.get_name()}")
        else:
            print("This item is on hold for another member.")

    def return_item(self, book_copy: 'BookCopy') -> None:
        print("Invalid action. Item is on hold, not checked out.")

    def place_hold(self, book_copy: 'BookCopy', member: 'Member') -> None:
        print("Item is already on hold.")

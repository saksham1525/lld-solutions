from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from member import Member
    from book_copy import BookCopy

class LibraryItem:
    """A catalog entry (e.g. a book or magazine title). Copies are the physical units members borrow."""

    def __init__(self, item_id: str, title: str, author_or_publisher: str):
        self.id = item_id
        self.title = title
        self.author_or_publisher = author_or_publisher
        self.copies: List['BookCopy'] = []
        self.observers: List['Member'] = []  # Observer pattern: members waiting for a copy to free up

    def add_copy(self, book_copy: 'BookCopy') -> None:
        self.copies.append(book_copy)

    def add_observer(self, member: 'Member') -> None:
        self.observers.append(member)

    def remove_observer(self, member: 'Member') -> None:
        if member in self.observers:
            self.observers.remove(member)

    def notify_observers(self) -> None:
        print(f"Notifying {len(self.observers)} observers for '{self.title}'...")
        for observer in self.observers.copy():  # copy() so removing a hold mid-loop is safe
            observer.update(self)

    def get_available_copy_count(self) -> int:
        return sum(1 for copy in self.copies if copy.is_available())

    def has_observers(self) -> bool:
        return len(self.observers) > 0

    def is_observer(self, member: 'Member') -> bool:
        return member in self.observers

    def get_id(self) -> str:
        return self.id

    def get_title(self) -> str:
        return self.title

    def get_author_or_publisher(self) -> str:
        return self.author_or_publisher

    def get_copies(self) -> List['BookCopy']:
        return self.copies

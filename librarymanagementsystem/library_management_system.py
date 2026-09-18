from typing import Dict, List
from library_item import LibraryItem
from member import Member
from book_copy import BookCopy
from search_strategy import SearchStrategy

class LibraryManagementSystem:
    def __init__(self):
        self.catalog: Dict[str, LibraryItem] = {}
        self.members: Dict[str, Member] = {}
        self.copies: Dict[str, BookCopy] = {}

    def add_item(self, item_id: str, title: str, author_or_publisher: str, num_copies: int) -> List[BookCopy]:
        item = LibraryItem(item_id, title, author_or_publisher)
        self.catalog[item_id] = item

        book_copies = []
        for i in range(num_copies):
            copy_id = f"{item_id}-c{i + 1}"
            book_copy = BookCopy(copy_id, item)
            self.copies[copy_id] = book_copy
            book_copies.append(book_copy)

        print(f"Added {num_copies} copies of '{title}'")
        return book_copies

    def add_member(self, member_id: str, name: str) -> Member:
        member = Member(member_id, name)
        self.members[member_id] = member
        return member

    def checkout(self, member_id: str, copy_id: str) -> None:
        member = self.members.get(member_id)
        book_copy = self.copies.get(copy_id)

        if member is not None and book_copy is not None:
            book_copy.checkout(member)
        else:
            print("Error: Invalid member or copy ID.")

    def return_item(self, copy_id: str) -> None:
        book_copy = self.copies.get(copy_id)
        if book_copy is not None:
            book_copy.return_item()
        else:
            print("Error: Invalid copy ID.")

    def place_hold(self, member_id: str, item_id: str) -> None:
        member = self.members.get(member_id)
        item = self.catalog.get(item_id)

        if member is not None and item is not None:
            # Place hold on any copy that is checked out
            for book_copy in item.get_copies():
                if not book_copy.is_available():
                    book_copy.place_hold(member)
                    break

    def search(self, query: str, strategy: SearchStrategy) -> List[LibraryItem]:
        return strategy.search(query, list(self.catalog.values()))

    def print_catalog(self) -> None:
        print("\n--- Library Catalog ---")
        for item in self.catalog.values():
            print(f"ID: {item.get_id()}, Title: {item.get_title()}, "
                  f"Author/Publisher: {item.get_author_or_publisher()}, "
                  f"Available: {item.get_available_copy_count()}")
        print("-----------------------\n")

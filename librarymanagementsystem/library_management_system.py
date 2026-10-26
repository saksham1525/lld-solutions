from datetime import date
from library_item import LibraryItem
from member import Member
from search_strategy import SearchStrategy

# Concurrency: two members can call checkout() on the same item at the same time.
# Both could see AvailableState and both "win", so one item ends up on two loans.
# The state check + state change must be atomic, e.g. a threading.Lock per item
# (or one lock in this facade). Not implemented here to keep the logic simple.
class LibraryManagementSystem:
    def __init__(self):
        self.items: dict[str, LibraryItem] = {}
        self.members: dict[str, Member] = {}

    def add_item(self, item_id: str, title: str, author: str) -> LibraryItem:
        item = LibraryItem(item_id, title, author)
        self.items[item_id] = item
        return item

    def remove_item(self, item_id: str) -> None:
        item = self.items.get(item_id)
        if item is None or not item.is_available():
            print("Error: Item not found or currently on loan.")
            return
        del self.items[item_id]

    def add_member(self, member_id: str, name: str) -> Member:
        member = Member(member_id, name)
        self.members[member_id] = member
        return member

    def checkout(self, member_id: str, item_id: str) -> None:
        member = self.members.get(member_id)
        item = self.items.get(item_id)
        if member is None or item is None:
            print("Error: Invalid member or item ID.")
            return
        item.checkout(member)

    def return_item(self, item_id: str, today: date | None = None) -> None:
        item = self.items.get(item_id)
        if item is None:
            print("Error: Invalid item ID.")
            return
        item.return_item(today or date.today())

    def search(self, query: str, strategy: SearchStrategy) -> list[LibraryItem]:
        return strategy.search(query, list(self.items.values()))

    def print_catalog(self) -> None:
        print("\n--- Library Catalog ---")
        for item in self.items.values():
            status = "Available" if item.is_available() else "Checked out"
            print(f"ID: {item.id}, Title: {item.title}, Author: {item.author}, {status}")
        print("-----------------------\n")

from datetime import date, timedelta
from library_management_system import LibraryManagementSystem
from search_strategy import SearchByTitleStrategy, SearchByAuthorStrategy

class LibraryManagementDemo:
    @staticmethod
    def main():
        library = LibraryManagementSystem()

        library.add_item("B001", "The Hobbit", "J.R.R. Tolkien")
        library.add_item("B002", "Dune", "Frank Herbert")
        library.add_item("B003", "Emma", "Jane Austen")
        library.add_item("B004", "Ulysses", "James Joyce")
        library.add_member("MEM01", "Alice")
        library.add_member("MEM02", "Bob")
        library.print_catalog()

        print("=== Search (Strategy) ===")
        for item in library.search("dune", SearchByTitleStrategy()):
            print(f"By title: {item.title}")
        for item in library.search("tolkien", SearchByAuthorStrategy()):
            print(f"By author: {item.title}")

        print("\n=== Checkout and Return (State) ===")
        library.checkout("MEM01", "B001")
        library.checkout("MEM02", "B001")  # fails: already checked out
        library.return_item("B001")
        library.return_item("B001")        # fails: not checked out

        print("\n=== Borrowing limit ===")
        for item_id in ["B001", "B002", "B003", "B004"]:
            library.checkout("MEM01", item_id)  # 4th fails: limit is 3

        print("\n=== Overdue fine ===")
        library.return_item("B002", today=date.today() + timedelta(days=17))  # returned 3 days late
        library.print_catalog()

if __name__ == "__main__":
    LibraryManagementDemo.main()

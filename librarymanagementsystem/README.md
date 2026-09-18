# Designing a Library Management System

## Requirements
1. The library management system should allow librarians to manage books, members, and borrowing activities.
2. The system should support adding, updating, and removing books from the library catalog.
3. Each book should have details such as title, author, ISBN, publication year, and availability status.
4. The system should allow members to borrow and return books.
5. Each member should have details such as name, member ID, contact information, and borrowing history.
6. The system should enforce borrowing rules, such as a maximum number of books that can be borrowed at a time and loan duration.
7. The system should handle concurrent access to the library catalog and member records.
8. The system should be extensible to accommodate future enhancements and new features.

## Classes, Interfaces and Enumerations
1. **LibraryItem** is a catalog entry (a title, e.g. "Dune") with an author/publisher and a list of physical `BookCopy` instances. Book vs. magazine is just data here (no behavioral difference), so there's a single class rather than subclasses per type.
2. **BookCopy** is the physical unit a member actually borrows. It holds an `ItemState` (State pattern) that governs what actions are legal on it.
3. **ItemState** (`AvailableState` / `CheckedOutState` / `OnHoldState`) encodes checkout/return/hold rules per state, so `BookCopy` doesn't need a pile of `if` statements to check what's currently allowed.
4. **Member** represents a library member and tracks their active `Loan`s. It's also the Observer in the Observer pattern below (`update()`).
5. `LibraryItem` is the Subject in an Observer pattern: members can `place_hold` on a checked-out item and are notified (`notify_observers`) when a copy is returned.
6. **SearchStrategy** (Strategy pattern) lets `LibraryManagementSystem.search()` take a pluggable search algorithm (`SearchByTitleStrategy`, `SearchByAuthorStrategy`) instead of hardcoding one.
7. **LibraryManagementSystem** is a plain facade over the catalog, members, and copies — it's instantiated directly by the caller (no Singleton), the way `ParkingLot`/`VendingMachine` are in the sibling projects.
8. **LibraryManagementSystemDemo** is the entry point and walks through searching, checkout/return, and holds.
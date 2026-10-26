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
1. **LibraryItem** is a single physical book/magazine (one item = one copy). It holds an `ItemState` (State pattern) and its current `Loan`.
2. **ItemState** in `states.py` (`AvailableState` / `CheckedOutState`) takes the item in its constructor, like the vending machine states, and encodes checkout/return rules per state. Checkout enforces `MAX_BOOKS_PER_MEMBER`; return computes the overdue fine.
3. **Loan** links an item to a member, with a `due_date` (`LOAN_DAYS` after checkout) and a `fine()` of `FINE_PER_DAY` per day late.
4. **Member** has a name, id, and active `Loan`s.
5. **SearchStrategy** (Strategy pattern) lets `search()` take a pluggable algorithm (`SearchByTitleStrategy`, `SearchByAuthorStrategy`).
6. **LibraryManagementSystem** is a plain facade over the items and members (no Singleton). Requirement 7 (concurrency) is explained in a comment there but not implemented.
7. **LibraryManagementSystemDemo** walks through search, checkout/return, the borrowing limit, and a fine.

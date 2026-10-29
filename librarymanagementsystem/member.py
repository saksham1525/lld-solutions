from loan import Loan

MAX_BOOKS_PER_MEMBER = 3

class Member:
    def __init__(self, member_id: str, name: str):
        self.id = member_id
        self.name = name
        # the loans this member currently has (not returned yet)
        self.loans: list[Loan] = []

    def can_borrow(self) -> bool:
        return len(self.loans) < MAX_BOOKS_PER_MEMBER

    def add_loan(self, loan: Loan) -> None:
        self.loans.append(loan)

    def remove_loan(self, loan: Loan) -> None:
        self.loans.remove(loan)

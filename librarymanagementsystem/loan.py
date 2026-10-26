from datetime import date, timedelta

LOAN_DAYS = 14
FINE_PER_DAY = 1

class Loan:
    def __init__(self, item, member):
        self.item = item
        self.member = member
        self.due_date = date.today() + timedelta(days=LOAN_DAYS)

    def fine(self, today: date) -> int:
        return max(0, (today - self.due_date).days) * FINE_PER_DAY

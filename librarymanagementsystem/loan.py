from datetime import date, timedelta

LOAN_DAYS = 14
FINE_PER_DAY = 1

class Loan:
    # A loan links one item to one member
    def __init__(self, item, member):
        self.item = item
        self.member = member
        # Due date is always checkout day + LOAN_DAYS, so it doesn't need to be passed in
        self.due_date = date.today() + timedelta(days=LOAN_DAYS)

    # today is passed in (instead of calling date.today() here) so we can test a late return
    def fine(self, today: date) -> int:
        return max(0, (today - self.due_date).days) * FINE_PER_DAY

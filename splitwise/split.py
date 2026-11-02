from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from user import User

class Split:
    def __init__(self, user: 'User', amount: float):
        self.user = user
        self.amount = amount
    
    def get_user(self) -> 'User':
        return self.user
    
    def get_amount(self) -> float:
        return self.amount
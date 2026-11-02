from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from user import User

class Transaction:
    def __init__(self, from_user: 'User', to_user: 'User', amount: float):
        self._from = from_user
        self.to = to_user
        self.amount = amount
    
    def __str__(self) -> str:
        return f"{self._from.get_name()} should pay {self.to.get_name()} ${self.amount:.2f}"
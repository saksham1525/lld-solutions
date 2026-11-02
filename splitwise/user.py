import uuid
from balance_sheet import BalanceSheet
    
class User:
    def __init__(self, name: str, email: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.balance_sheet = BalanceSheet(self)
    
    def get_id(self) -> str:
        return self.id
    
    def get_name(self) -> str:
        return self.name
    
    def get_balance_sheet(self) -> 'BalanceSheet':
        return self.balance_sheet
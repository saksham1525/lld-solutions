from datetime import datetime
from typing import List, Optional
from user import User
from split import Split
from split_strategy import SplitStrategy

class Expense:
    def __init__(self, builder: 'ExpenseBuilder'):
        self.id = builder.id
        self.description = builder.description
        self.amount = builder.amount
        self.paid_by = builder.paid_by
        self.timestamp = datetime.now()
        
        # Use the strategy to calculate splits
        self.splits = builder.split_strategy.calculate_splits(
            builder.amount, builder.paid_by, builder.participants, builder.split_values
        )
    
    def get_id(self) -> str:
        return self.id
    
    def get_description(self) -> str:
        return self.description
    
    def get_amount(self) -> float:
        return self.amount
    
    def get_paid_by(self) -> User:
        return self.paid_by
    
    def get_splits(self) -> List[Split]:
        return self.splits
    
    class ExpenseBuilder:
        def __init__(self):
            self.id: Optional[str] = None
            self.description: Optional[str] = None
            self.amount: Optional[float] = None
            self.paid_by: Optional[User] = None
            self.participants: Optional[List[User]] = None
            self.split_strategy: Optional[SplitStrategy] = None
            self.split_values: Optional[List[float]] = None
        
        def set_id(self, expense_id: str) -> 'Expense.ExpenseBuilder':
            self.id = expense_id
            return self
        
        def set_description(self, description: str) -> 'Expense.ExpenseBuilder':
            self.description = description
            return self
        
        def set_amount(self, amount: float) -> 'Expense.ExpenseBuilder':
            self.amount = amount
            return self
        
        def set_paid_by(self, paid_by: User) -> 'Expense.ExpenseBuilder':
            self.paid_by = paid_by
            return self
        
        def set_participants(self, participants: List[User]) -> 'Expense.ExpenseBuilder':
            self.participants = participants
            return self
        
        def set_split_strategy(self, split_strategy: SplitStrategy) -> 'Expense.ExpenseBuilder':
            self.split_strategy = split_strategy
            return self
        
        def set_split_values(self, split_values: List[float]) -> 'Expense.ExpenseBuilder':
            self.split_values = split_values
            return self
        
        def build(self) -> 'Expense':
            if self.split_strategy is None:
                raise ValueError("Split strategy is required.")
            return Expense(self)
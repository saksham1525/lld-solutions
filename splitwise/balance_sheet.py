import threading
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from user import User

class BalanceSheet:
    def __init__(self, user: 'User'):
        self.owner = user
        self.balances: Dict['User', float] = {}
        self.lock = threading.Lock()
    
    def get_balances(self) -> Dict['User', float]:
        return self.balances
    
    def adjust_balance(self, other_user: 'User', amount: float):
        with self.lock:
            if self.owner == other_user:
                return  # Cannot owe yourself
            
            if other_user in self.balances:
                self.balances[other_user] += amount
            else:
                self.balances[other_user] = amount
    
    def show_balances(self):
        print(f"--- Balance Sheet for {self.owner.get_name()} ---")
        if not self.balances:
            print("All settled up!")
            return
        
        total_owed_to_me = 0
        total_i_owe = 0
        
        for other_user, amount in self.balances.items():
            if amount > 0.01:
                print(f"{other_user.get_name()} owes {self.owner.get_name()} ${amount:.2f}")
                total_owed_to_me += amount
            elif amount < -0.01:
                print(f"{self.owner.get_name()} owes {other_user.get_name()} ${-amount:.2f}")
                total_i_owe += (-amount)
        
        print(f"Total Owed to {self.owner.get_name()}: ${total_owed_to_me:.2f}")
        print(f"Total {self.owner.get_name()} Owes: ${total_i_owe:.2f}")
        print("---------------------------------")
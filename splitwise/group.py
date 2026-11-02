import uuid
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from user import User

class Group:
    def __init__(self, name: str, members: List['User']):
        self.id = str(uuid.uuid4())
        self.name = name
        self.members = members
    
    def get_id(self) -> str:
        return self.id
    
    def get_name(self) -> str:
        return self.name
    
    def get_members(self) -> List['User']:
        return self.members.copy()
from abc import ABC, abstractmethod
from library_item import LibraryItem

class SearchStrategy(ABC):
    @abstractmethod
    def search(self, query: str, items: list[LibraryItem]) -> list[LibraryItem]:
        pass

class SearchByTitleStrategy(SearchStrategy):
    def search(self, query: str, items: list[LibraryItem]) -> list[LibraryItem]:
        return [item for item in items if query.lower() in item.title.lower()]

class SearchByAuthorStrategy(SearchStrategy):
    def search(self, query: str, items: list[LibraryItem]) -> list[LibraryItem]:
        return [item for item in items if query.lower() in item.author.lower()]

class Item:
    def __init__(self, code: str, name: str, price: int, quantity: int):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> int:
        return self.price

    def is_available(self) -> bool:
        return self.quantity > 0

    def reduce_stock(self) -> None:
        self.quantity -= 1

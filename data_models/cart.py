from dataclasses import dataclass

@dataclass
class Item:
    productId: int
    quantity: int

@dataclass
class Cart:
    userId: int
    date: str
    products: list[Item]



from dataclasses import dataclass

@dataclass
class Order:
    price: float
    size: float
    side: str  # 'bid' or 'ask'
    timestamp: float = None
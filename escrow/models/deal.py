from dataclasses import dataclass
from typing import Optional

@dataclass
class Deal:
    chat_id: int
    buyer: Optional[str] = None
    seller: Optional[str] = None
    quantity: Optional[float] = None
    rate: Optional[float] = None
    condition: Optional[str] = None
    fee_policy: Optional[str] = None
    buyer_confirmed: bool = False
    seller_confirmed: bool = False
    status: str = "pending"
    
    def is_ready(self) -> bool:
        return all([self.buyer, self.seller, self.quantity, self.rate, self.condition, self.fee_policy])
    
    def both_confirmed(self) -> bool:
        return self.buyer_confirmed and self.seller_confirmed

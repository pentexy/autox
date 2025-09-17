from dataclasses import dataclass

@dataclass
class User:
    user_id: int
    username: str
    role: str  # 'buyer' or 'seller'

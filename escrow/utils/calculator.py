from config import ESCROW_FEE_PERCENTAGE

def calculate_fees(quantity: float, rate: float, fee_policy: str) -> dict:
    base_amount = quantity * rate
    fee_amount = base_amount * (ESCROW_FEE_PERCENTAGE / 100)
    
    if fee_policy == "buyer_pays":
        return {
            "base_amount": base_amount,
            "fee_amount": fee_amount,
            "total_amount": base_amount + fee_amount,
            "buyer_pays": base_amount + fee_amount,
            "seller_receives": base_amount
        }
    elif fee_policy == "split":
        half_fee = fee_amount / 2
        return {
            "base_amount": base_amount,
            "fee_amount": fee_amount,
            "total_amount": base_amount + fee_amount,
            "buyer_pays": base_amount + half_fee,
            "seller_receives": base_amount - half_fee
        }
    return {}

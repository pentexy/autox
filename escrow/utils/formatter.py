def bold(text: str) -> str:
    return f"<b>{text}</b>"

def italic(text: str) -> str:
    return f"<i>{text}</i>"

def code(text: str) -> str:
    return f"<code>{text}</code>"

def pre(text: str) -> str:
    return f"<pre>{text}</pre>"

def format_deal_preview(quantity, rate, condition) -> str:
    return f"""
📋 {bold('Deal Form Preview')}

{bold('Quantity:')} {code(str(quantity))}
{bold('Rate:')} {code(str(rate))}
{bold('Condition:')} {code(condition)}
"""

def format_fee_summary(quantity, rate, fee_policy, fee_details) -> str:
    base = quantity * rate
    
    if fee_policy == "buyer_pays":
        return f"""
💳 {bold('Fee Summary')} ({italic('Buyer Pays Fees')})

{bold('Base Amount:')} {code(str(round(base, 2)))}
{bold('Escrow Fee (1%):')} {code(str(round(fee_details['fee_amount'], 2)))}
{bold('Total Amount:')} {code(str(round(fee_details['total_amount'], 2)))}

{bold('Buyer will pay:')} {code(str(round(fee_details['total_amount'], 2)))}
{bold('Seller will receive:')} {code(str(round(base, 2)))}
"""
    else:
        return f"""
💳 {bold('Fee Summary')} ({italic('Split Fees 50/50')})

{bold('Base Amount:')} {code(str(round(base, 2)))}
{bold('Escrow Fee (1%):')} {code(str(round(fee_details['fee_amount'], 2)))}
{bold('Total Amount:')} {code(str(round(fee_details['total_amount'], 2)))}

{bold('Buyer will pay:')} {code(str(round(fee_details['buyer_pays'], 2)))}
{bold('Seller will receive:')} {code(str(round(fee_details['seller_receives'], 2)))}
"""

def format_confirmation_message(deal, fee_details) -> str:
    base = deal.quantity * deal.rate
    
    if deal.fee_policy == "buyer_pays":
        payment_info = f"💳 {bold('Buyer pays:')} {code(str(round(fee_details['total_amount'], 2)))}"
    else:
        payment_info = f"💳 {bold('Buyer pays:')} {code(str(round(fee_details['buyer_pays'], 2)))}"
    
    return f"""
✅ {bold('Deal Ready for Confirmation')}

{bold('Parties:')}
👤 {bold('Buyer:')} {code('@' + deal.buyer)}
👤 {bold('Seller:')} {code('@' + deal.seller)}

{bold('Terms:')}
📦 {bold('Quantity:')} {code(str(deal.quantity))}
💰 {bold('Rate:')} {code(str(deal.rate))}
📝 {bold('Condition:')} {code(deal.condition)}

{bold('Financials:')}
💵 {bold('Base Amount:')} {code(str(round(base, 2)))}
🏷️ {bold('Fee Policy:')} {code('Buyer pays all' if deal.fee_policy == 'buyer_pays' else 'Split 50/50')}
{payment_info}

{bold('Please confirm the deal:')}
"""

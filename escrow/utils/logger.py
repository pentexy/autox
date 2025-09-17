import telegram
from config import BOT_TOKEN, LOG_GROUP_ID
from utils.formatter import bold, code
from utils.calculator import calculate_fees

async def log_to_group(deal, buyer_username: str, seller_username: str):
    bot = telegram.Bot(token=BOT_TOKEN)
    
    fee_details = calculate_fees(deal.quantity, deal.rate, deal.fee_policy)
    
    if deal.fee_policy == "buyer_pays":
        fee_policy = "Buyer pays fees"
    else:
        fee_policy = "Split fees 50/50"
    
    message = f"""
📑 {bold('Escrow Created')}

{bold('Parties:')}
👤 {bold('Buyer:')} @{buyer_username}
👤 {bold('Seller:')} @{seller_username}

{bold('Terms:')}
📦 {bold('Quantity:')} {code(str(deal.quantity))}
💰 {bold('Rate:')} {code(str(deal.rate))}
📝 {bold('Condition:')} {code(deal.condition)}

{bold('Financials:')}
💵 {bold('Base Amount:')} {code(str(round(fee_details['base_amount'], 2)))}
🏷️ {bold('Fee Policy:')} {code(fee_policy)}
💸 {bold('Fee Amount:')} {code(str(round(fee_details['fee_amount'], 2)))}
💳 {bold('Total Amount:')} {code(str(round(fee_details['total_amount'], 2)))}
👤 {bold('Buyer Pays:')} {code(str(round(fee_details['buyer_pays'], 2)))}
👤 {bold('Seller Receives:')} {code(str(round(fee_details['seller_receives'], 2)))}

{bold('Status:')} ⏳ Awaiting Payment
"""
    
    await bot.send_message(
        chat_id=LOG_GROUP_ID, 
        text=message,
        parse_mode='HTML'
    )

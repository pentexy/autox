from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import log_to_group
from utils.formatter import bold, code

async def handle_confirmation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    user = query.from_user
    deal = active_deals.get(chat_id)
    
    if not deal:
        await query.answer("❌ No active deal")
        return
    
    username = user.username or user.first_name
    
    if "confirm_buyer" in query.data:
        if username != deal.buyer:
            await query.answer("❌ Only the buyer can confirm as buyer")
            return
        deal.buyer_confirmed = True
        await query.answer("✅ Buyer confirmed")
    elif "confirm_seller" in query.data:
        if username != deal.seller:
            await query.answer("❌ Only the seller can confirm as seller")
            return
        deal.seller_confirmed = True
        await query.answer("✅ Seller confirmed")
    
    # Update message to show confirmation status
    confirmation_status = f"""
{bold('Confirmation Status:')}
✅ {bold('Buyer:')} {code('Confirmed' if deal.buyer_confirmed else 'Pending')}
✅ {bold('Seller:')} {code('Confirmed' if deal.seller_confirmed else 'Pending')}
"""
    
    if deal.both_confirmed():
        # Log to group
        await log_to_group(deal, deal.buyer, deal.seller)
        
        await query.edit_message_text(
            f"""
🎉 {bold('Deal Confirmed by Both Parties!')}

{confirmation_status}

📦 {bold('Next Steps:')}
Payment process will be handled here...

We'll notify both parties when the escrow is set up.
""",
            parse_mode='HTML'
        )
    else:
        # Update the message to show who has confirmed so far
        message_parts = query.message.text.split('\n\n')
        original_message = '\n\n'.join(message_parts[:-1])  # Remove the old confirmation status
        
        await query.edit_message_text(
            original_message + confirmation_status,
            reply_markup=query.message.reply_markup,
            parse_mode='HTML'
        )

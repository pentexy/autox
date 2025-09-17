from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from models.deal import Deal
from utils.formatter import bold, code

async def handle_role_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    user = query.from_user
    
    deal = active_deals.get(chat_id)
    if not deal:
        await query.answer("❌ No active deal found. Start with /deal")
        return
    
    username = user.username or user.first_name
    
    if "role_buyer" in query.data:
        deal.buyer = username
        await query.answer("✅ You're set as Buyer")
    elif "role_seller" in query.data:
        deal.seller = username
        await query.answer("✅ You're set as Seller")
    
    # Update the message with current status
    status_text = f"""
{bold('Buyer:')} {code(deal.buyer if deal.buyer else 'Not set yet')}
{bold('Seller:')} {code(deal.seller if deal.seller else 'Not set yet')}
"""
    
    # Check if both roles are set
    if deal.buyer and deal.seller:
        keyboard = None
        message = f"""
✅ {bold('Roles Confirmed!')}

{status_text}

📋 {bold('Next Step:')}
Please send the deal details in this format:

{code('quantity : rate : condition')}

{italic('Example:')} {code('100 : 0.85 : Brand new, sealed')}
"""
    else:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("👤 I'm the Buyer", callback_data="role_buyer")],
            [InlineKeyboardButton("👤 I'm the Seller", callback_data="role_seller")]
        ])
        message = f"""
🤝 {bold('Auto Escrow Deal Setup')}

Please choose your role:

{status_text}
"""
    
    await query.edit_message_text(
        message,
        reply_markup=keyboard,
        parse_mode='HTML'
    )

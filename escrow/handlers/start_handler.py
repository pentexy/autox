from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from models.deal import Deal
from utils.formatter import bold, code

# In-memory storage (replace with database in production)
active_deals = {}

async def deal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    
    # Initialize new deal
    active_deals[chat_id] = Deal(chat_id=chat_id)
    
    keyboard = [
        [InlineKeyboardButton("👤 I'm the Buyer", callback_data="role_buyer")],
        [InlineKeyboardButton("👤 I'm the Seller", callback_data="role_seller")]
    ]
    
    message = f"""
🤝 {bold('Auto Escrow Deal Setup')}

Please choose your role:

{bold('Buyer:')} {code('Not set yet')}
{bold('Seller:')} {code('Not set yet')}
"""
    
    await update.message.reply_text(
        message,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='HTML'
    )
